# Checkers AI with TensorFlow
A two-player Checkers game where you compete against an AI powered by TensorFlow. The AI learns to make valid moves through machine learning rather than hardcoded rules.

## Example Board
<img src="./Images:BaseBoard2.png" alt="Checkers Board" width="300">

## Features
- Player vs AI gameplay
- Jump and multi-jump captures
- King promotion mechanics
- TensorFlow-powered AI decision making
- Terminal-based interface with color-coded pieces

## How to Play
1. Run `python play.py`
2. Enter moves using row and column numbers
3. Capture pieces by jumping over them
4. Reach the opposite end to get kinged
5. Eliminate all AI pieces to win

## Project Structure
```bash
checkers-ai-tensorflow/
├── checkers_ai.py      # AI logic, board setup, model training, and prediction
│   ├── initial_board()       # Generates starting board
│   ├── flatten_board()       # Flattens board for ML input
│   ├── build_model()         # Builds TensorFlow model
│   ├── train()               # Trains and saves the model
│   └── predict_move()        # Outputs best move from model
│
├── play.py             # Main CLI game loop
│   ├── render()               # Prints ASCII board with colors
│   ├── player_move()          # Player input and rules
│   ├── ai_move()              # AI move logic using model
│   └── check_game_over()      # Detects end of game
│
├── model/              # Trained model folder (optional)
    └── checkers_ai_model.h5   # Saved TensorFlow model
```

## Source Files
- [checkers_ai.py](checkers_ai.py) — 
- [play.py](play.py) —
