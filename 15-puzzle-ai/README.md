# 15 Puzzle Solver (A* Search)

This project is a Python implementation of the **15 Puzzle Solver** using the A* search algorithm with the **Manhattan distance heuristic**.

## 📌 About the 15 Puzzle

The 15 puzzle is a classic sliding puzzle that’s played on a 4x4 grid with 15 numbered tiles and one empty space ('0' in this code).  
The goal is to slide the tiles into order from 1 to 15, with the blank tile at the bottom-right.

## Example Start Board
  1 2 3 4
  5 6 7 8
  9 10 11 12
  13 14 15 0

## 🚀 Features

- Solves any valid 15-puzzle board using **A\*** search.
- Uses the **Manhattan distance** to estimate how far each tile is from where it should be.
- Prints each step of the solution in the terminal so you can follow along.
- Tells you how many moves it took to solve.

## 📁 File Structure

- `solver.py` – Main file that includes:
  - The `Puzzle` class
  - The A\* search logic in `solve()`
  - The path reconstruction function
  - A helper to print the board nicely

## 🧠 Algorithm Details

- **Heuristic (h)**: Sum of Manhattan distances between each tile and its goal spot.
- **Cost (g)**: Number of moves taken so far.
- **Total (f = g + h)**: This score decides which board gets explored next.

## 🔧 How to Run

Make sure you’re using Python 3. Then just run:

```bash
python solver.py
