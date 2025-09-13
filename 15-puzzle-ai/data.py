import random
from solver import solve, Puzzle
import csv

# Returns a scrambled board by applying n random moves
def scramble_board(n=20):
    board = list(range(1, 16)) + [0]
    puzzle = Puzzle(board)
    for _ in range(n):
        neighbors = puzzle.neighbors()
        puzzle = random.choice(neighbors)
    return puzzle.board


# Figure out the first move in the solution
def get_first_move(solution):
    if len(solution) < 2:
        return None
    empty1 = solution[0].index(0)
    empty2 = solution[1].index(0)
    diff = empty2 - empty1
    return {
        -4: 'up', 4: 'down', -1: 'left', 1: 'right'
    }.get(diff, None)

# Create CSV: 16 board positions + 1 label
with open('train_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for _ in range(1000):  # generate 1000 boards
        board = scramble_board(20)
        solution = solve(board)
        move = get_first_move(solution)
        if move:
            writer.writerow(board + [move])
