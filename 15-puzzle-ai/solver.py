import heapq

class Puzzle:
    def __init__(self, board, moves=0, prev=None):
        self.board = board  # flat list of 16 numbers
        self.moves = moves  # g(n)
        self.prev = prev    # to reconstruct path
        self.empty = board.index(0)  # 0 = blank tile

    def __lt__(self, other):
        return self.moves + self.heuristic() < other.moves + other.heuristic()

    def heuristic(self):
        # Manhattan Distance
        dist = 0
        for i, val in enumerate(self.board):
            if val == 0:
                continue
            target = val - 1
            x1, y1 = i % 4, i // 4
            x2, y2 = target % 4, target // 4
            dist += abs(x1 - x2) + abs(y1 - y2)
        return dist

    def is_solved(self):
        return self.board == list(range(1, 16)) + [0]

    def neighbors(self):
        # Generate valid next moves
        moves = []
        x, y = self.empty % 4, self.empty // 4
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # L, R, U, D
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                idx = ny * 4 + nx
                new_board = self.board[:]
                new_board[self.empty], new_board[idx] = new_board[idx], new_board[self.empty]
                moves.append(Puzzle(new_board, self.moves + 1, self))
        return moves

def solve(start_board):
    start = Puzzle(start_board)
    visited = set()
    heap = []
    heapq.heappush(heap, (start.moves + start.heuristic(), start))

    while heap:
        _, current = heapq.heappop(heap)
        board_tuple = tuple(current.board)

        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        if current.is_solved():
            return reconstruct_path(current)

        for neighbor in current.neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(heap, (neighbor.moves + neighbor.heuristic(), neighbor))

    return None

def reconstruct_path(puzzle):
    path = []
    while puzzle:
        path.append(puzzle.board)
        puzzle = puzzle.prev
    return path[::-1]

def print_board(board):
    for i in range(0, 16, 4):
        print(board[i:i+4])

if __name__ == "__main__":
    start_board = [
        5, 1, 2, 4,
        9, 6, 3, 8,
        13, 10, 7, 12,
        0, 14, 11, 15
    ]
    solution = solve(start_board)
    if solution:
        for step in solution:
            print_board(step)
            print("----")
        print(f"Solved in {len(solution) - 1} moves.")
    else:
        print("No solution found.")
