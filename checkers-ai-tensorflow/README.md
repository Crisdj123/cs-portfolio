# Checkers AI with TensorFlow

This project is a two-player Checkers game where the player competes against a basic AI powered by TensorFlow. 
The goal is to showcase game logic, player interaction, and a machine learning model making valid (if not optimal) moves. 
The AI can move, capture, and promote to king based on learned behavior or simple heuristics.


## 🎮 Features

- Turn-based checkers gameplay (Player vs AI)  
- Jump and multi-jump capture logic  
- King promotion for both player and AI  
- Basic AI using a trained TensorFlow model  
- Manual move input via terminal  
- Color-coded board rendering in ASCII  
- Game-over detection


## 🤖 AI Overview

The AI selects moves using a TensorFlow model that was trained on past gameplay data or hardcoded rules. 
The model takes the board state as input and outputs a move. If no valid moves are available, the AI forfeits.


## 🧩 Project Structure

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

## 🛠 Usage

Run the game:

Enter your moves by specifying row and column numbers.
Capture enemy pieces by jumping.
Get kinged by reaching the opposite end of the board.
Win by eliminating all AI pieces or blocking all its moves.
