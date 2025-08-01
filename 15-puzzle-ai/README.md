# 15 Puzzle Solver (A* Search)

This project is a Python implementation of the **15 Puzzle Solver** using the A* search algorithm with the **Manhattan distance heuristic**.

## 📌 About the 15 Puzzle

The 15 puzzle is a sliding tile game played on a 4x4 grid with 15 numbered tiles and one empty space (represented as `0` in this project).  
The goal is to arrange the numbers in order from 1 to 15, with the blank tile in the bottom-right corner.

## Example Start and End Board
<pre>
Start Board       |    End Board
6   2   3   4     |    1   2   3   4
1   9  10   7     |    5   6   7   8
13  5   0   8     |    9  10  11  12
11 14  15  12     |    13 14  15   0
</pre>

## 🚀 Features

- Solves any valid (solvable) 15-puzzle board using A* search
- Uses Manhattan distance as the heuristic for tile positioning
- Prints each step of the solution in the terminal so you can follow along
- Displays total move count and solve time
- Adjustable difficulty by changing shuffle depth

## File Structure
```bash
15puzzle-a-star/
├── solver.py              # Main puzzle solver using A* and Manhattan Distance
    ├── Puzzle                  # Board class with methods for movement and state checking
    │   ├── heuristic()              # Manhattan distance cost function
    │   ├── is_solved()             # Checks if the puzzle is complete
    │   └── neighbors()             # Generates valid tile moves
    ├── solve()                # A* search algorithm to find optimal solution
    ├── generate_board()       # Scrambles the board by making N valid moves
    ├── reconstruct_path()     # Rebuilds solution path from end to start
    ├── print_board()          # Prints the board in 4x4 format
    └── is_solvable()          # (Not used, but checks solvability by inversion count)
```

## 🧠 Algorithm Details

- **Heuristic (h)**: Sum of Manhattan distances between each tile and its goal spot.
- **Cost (g)**: Number of moves taken so far.
- **Total (f = g + h)**: This score decides which board gets explored next.

## How to Run

Make sure you’re using Python 3. Then just run:

```bash
python3 solver.py
```
## Full Source Code
```bash
import heapq
import random
import time

# Puzzle class handles all the board logic and A* stuff
class Puzzle:
    def __init__(self, board, moves=0, prev=None):
        self.board = board  # 1D list of 16 tiles (0 is blank)
        self.moves = moves  # how many moves so far
        self.prev = prev    # for tracing back the path
        self.empty = board.index(0)  # find the position of the blank
        
    def __lt__(self, other):
        # needed for heapq to compare puzzles (by f(n) = g(n) + h(n))
        return self.moves + self.heuristic() < other.moves + other.heuristic()

    def heuristic(self):
        # Manhattan Distance (how far each tile is from its goal spot)
        dist = 0
        for i, val in enumerate(self.board):
            if val == 0:
                continue  # skip the blank
            target = val - 1
            x1, y1 = i % 4, i // 4
            x2, y2 = target % 4, target // 4
            dist += abs(x1 - x2) + abs(y1 - y2)
        return dist

    def is_solved(self):
        # check if the board is in solved order
        return self.board == list(range(1, 16)) + [0]

    def neighbors(self):
        # generate all possible moves from current state
        moves = []
        x, y = self.empty % 4, self.empty // 4
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                idx = ny * 4 + nx
                new_board = self.board[:]  # make a copy
                # swap the blank with the neighbor tile
                new_board[self.empty], new_board[idx] = new_board[idx], new_board[self.empty]
                moves.append(Puzzle(new_board, self.moves + 1, self))
        return moves

# A* algorithm to solve the puzzle
def solve(start_board):
    start = Puzzle(start_board)
    visited = {}  # store states we've seen with the lowest cost
    heap = []
    heapq.heappush(heap, (start.moves + start.heuristic(), start))

    start_time = time.time()

    while heap:
        # timeout just in case it takes way too long
        if time.time() - start_time > 60:
            print("Timed out.")
            return None

        _, current = heapq.heappop(heap)
        board_tuple = tuple(current.board)

        # skip if we already visited this board with fewer moves
        if board_tuple in visited and visited[board_tuple] <= current.moves:
            continue
        visited[board_tuple] = current.moves

        if current.is_solved():
            return reconstruct_path(current)

        for neighbor in current.neighbors():
            neighbor_tuple = tuple(neighbor.board)
            if neighbor_tuple not in visited or neighbor.moves < visited[neighbor_tuple]:
                heapq.heappush(heap, (neighbor.moves + neighbor.heuristic(), neighbor))

    return None  # if no solution found (shouldn't happen if board is solvable)

# generates a random solvable board by making N random valid moves
def generate_board(shuffle_moves=350):
    board = list(range(1, 16)) + [0]  # start from solved state
    puzzle = Puzzle(board)

    for _ in range(shuffle_moves):
        neighbors = puzzle.neighbors()
        puzzle = random.choice(neighbors)  # pick a random legal move

    return puzzle.board

# used for full shuffles (not needed here but useful for reference)
def is_solvable(board):
    inv_count = 0
    for i in range(15):
        for j in range(i + 1, 16):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                inv_count += 1
    blank_row = 4 - (board.index(0) // 4)
    return (inv_count + blank_row) % 2 == 0

# backtracks from the solved board to the start to get the path
def reconstruct_path(puzzle):
    path = []
    while puzzle:
        path.append(puzzle.board)
        puzzle = puzzle.prev
    return path[::-1]  # reverse so it's start → goal

# prints the board nicely
def print_board(board):
    for i in range(0, 16, 4):
        print(board[i:i+4])

if __name__ == "__main__":
    start_board = generate_board(shuffle_moves=350)  # change shuffle_moves to make it easier/harder

    print("Starting board:")
    print_board(start_board)
    print("----")

    print("Solving...")

    start_time = time.time()
    solution = solve(start_board)
    end_time = time.time()
    duration = end_time - start_time

    if solution:
        for step in solution:
            print_board(step)
            print("----")
        print(f"Solved in {len(solution) - 1} moves.")
    else:
        print("No solution found.")  # could happen if timeout triggers

    print(f"Took {duration:.2f} seconds.")
