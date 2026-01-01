# Pygame Snake Game

A retro version of Snake built using Python and Pygame. Created as a 3-person group project — 
I served as the **lead programmer**, responsible for the main game logic, collision, and scoring.

## About the Game

The goal of the game is simple: control the snake using the arrow keys, collect apples (red squares), and avoid colliding with yourself or the walls.  
Each apple increases your score and adds length to the snake. The game keeps track of your high score using a local save file.

The grid updates in real time, and the longer you survive, the more challenging it becomes to avoid yourself.

## Features

- Real-time movement and smooth snake growth
- Collision detection for both self and boundaries
- Apple placement with proper grid alignment
- Score and timer display on screen
- High score saved and loaded from `Score.txt`
- Clean 10x10 grid visualized using lines
- Restart and quit functionality after game over

## Controls

- Arrow Keys or W, A, S, D — Move Up/Down/Left/Right

- R — Restart after Game Over

- Q — Quit after Game Over

- Esc / Window Close — Exit game

## How to Run
1. Install Python 3 and Pygame:
2. Run the game:

## My Contributions
- Game loop and event handling
- Score tracking and file read/write
- Collision logic and snake movement

## Built For
CSE1321 Final Project @ Kennesaw State University (Fall 2024)

## Source Files
- [snake.py](snake.py) — Main game (loop, input, collisions, scoring, high score)
- [Score.txt](Score.txt) — High score storage (auto-created/updated)
- [assets/](assets/) — (optional) music/sfx if added later
