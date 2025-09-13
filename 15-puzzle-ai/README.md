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
│   ├── Puzzle             # Board class with methods for movement and state checking
│   │   ├── heuristic()        # Manhattan distance cost function
│   │   ├── is_solved()        # Checks if the puzzle is complete
│   │   └── neighbors()        # Generates valid tile moves
│   ├── solve()             # A* search algorithm to find optimal solution
│   ├── generate_board()    # Scrambles the board by making N valid moves
│   ├── reconstruct_path()  # Rebuilds solution path from end to start
│   ├── print_board()       # Prints the board in 4x4 format
│   └── is_solvable()       # (Not used, checks solvability by inversion count)
│
├── data.py                # Utility for generating training data (CSV)
│   ├── scramble_board()    # Scrambles a board by applying random moves
│   ├── get_first_move()    # Extracts the first move from a solution
│   └── (main script)       # Generates train_data.csv with 1000 boards + labels
│
└── train_data.csv         # Auto-generated dataset: 16 board positions + 1 move label
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
- [solver.py](solver.py) — A* solver with Manhattan distance  
- [data.py](data.py) — Dataset generator for training (creates `train_data.csv`)  
