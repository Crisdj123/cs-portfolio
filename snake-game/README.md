# 🐍 Pygame Snake Game

A retro version of Snake built using Python and Pygame. Created as a group project with 4 students — 
I served as the **lead programmer**, responsible for the main game logic, collision, and scoring.

## 📌 About the Game

The goal of the game is simple: control the snake using the arrow keys, collect apples (red squares), and avoid colliding with yourself or the walls.  
Each apple increases your score and adds length to the snake. The game keeps track of your high score using a local save file.

The grid updates in real time, and the longer you survive, the more challenging it becomes to avoid yourself.

## 🚀 Features

- Real-time movement and smooth snake growth
- Collision detection for both self and boundaries
- Apple placement with proper grid alignment
- Score and timer display on screen
- High score saved and loaded from `Score.txt`
- Clean 10x10 grid visualized using lines
- Restart and quit functionality after game over


## How to Run
1. Install Python 3 and Pygame:
2. Run the game:

## My Contributions
- Game loop and event handling
- Score tracking and file read/write
- Collision logic and snake movement

## Built For
CSE1321 Final Project @ Kennesaw State University (Fall 2024)

## Full Source Code
```bash
import pygame, sys, random
pygame.init()

startTime = pygame.time.get_ticks()
endTime = None

# Cristian: Function to create, open, and read the file
def startFile(name):
    highscore = 0
    # Cristian: Open in append plus (read and write into the file)
    file = open(name, "a")
    file.close()
    file = open(name, 'r')
    line = file.readline().strip()
    if line != "":
        highscore = int(line)

    file.close()
    return highscore

# Cristian: Function to write to the file if needed.
def updateScore(name, highscore):
    file = open(name, "w")
    file.write(str(highscore))
    file.close()

# Cristian: Colors
orange = (255, 175, 20)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#Josiah: Loads and plays background music
#pygame.mixer.music.load("game-music-loop-7-145285.mp3")
#pygame.mixer.music.play(-1)  # Play the music infinitely

# Josiah: Loads the sound effect for when the snake eats an apple
#eat_sound = pygame.mixer.Sound("carrotnom-92106.mp3")

# Generate random positions for the red square (rect2) within the screen dimensions,
# ensuring they are multiples of 10 for grid alignment
randy = random.randint(1, 49) * 10
randx = random.randint(1, 74) * 10

screen = pygame.display.set_mode((750, 500))
# Faaris: Makes the font for displaying the score and timer
game_font = pygame.font.Font(None, 36)

# Cristian: size of snake/one piece
snakeSize = 10

# Head Surf and rect
surf = pygame.Surface((10, 10))
surf.fill(color=orange)
rect = surf.get_rect(topleft=(370, 250))  # Set the initial position of the green square
# Cristian: Snake list of segments and their surfaces
snakeRects = [rect]
snakeSurfs = [surf]

# Create a red square (surf2) with dimensions 10x10 pixels and place it at a random position
surf2 = pygame.Surface((10, 10))
surf2.fill(color=red)
rect2 = surf2.get_rect(topleft=(randx, randy))  # Set the initial random position of the red square

direction = 'Right'  # Set the initial direction to "Right"
move = 10  # Distance moved in each step
x = 0  # Horizontal movement
y = 0  # Vertical movement
speed = 50  # Controls the game speed (lower value = faster movement)
counter = 1  # Used to manage the movement speed
score = 0  # Tracks the score and how much the snake should scale by
gameOver = False  # Tracks if a rule is broken

begin_ticks = pygame.time.get_ticks()  # Faaris: This gets the start time
reset_head = pygame.Rect(370, 250, snakeSize, snakeSize)  # New head for restarting the game
highScore = startFile("Score.txt")  # Cristian: Tracks current highest score

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Control the movement of the green square at intervals determined by the speed
    if counter % (speed + 1) == 0:
        # Cristian: Move each piece of snake (Allows fluid movement)
        for i in range(len(snakeRects) - 1, 0, -1):
            snakeRects[i].topleft = snakeRects[i-1].topleft  # Cristian: Every piece is moved to where the one before is/was
        snakeRects[0] = snakeRects[0].move(x, y)  # Cristian: Finish by moving the head

        counter = 1  # Reset counter after a move
    counter += 1  # Increment counter to manage speed timing

    # Cristian: Check for collision between the green and red squares
    if not gameOver and rect2.colliderect(snakeRects[0]):
        # Reposition the red square at a new random location
        randy = random.randint(1, 49) * 10
        randx = random.randint(1, 74) * 10
        rect2 = surf2.get_rect(topleft=(randx, randy))  # Update red square position
        score += 4  # Increase score when getting an apple
        print(score)

        # Add 4 pieces to the snake without overlapping
        for i in range(4):
            # Set new segment position based on the last segment and the current direction
            last_rect = snakeRects[-1]
            if direction == 'Right':
                new_rect = last_rect.move(-snakeSize, 0)
            elif direction == 'Left':
                new_rect = last_rect.move(snakeSize, 0)
            elif direction == 'Up':
                new_rect = last_rect.move(0, snakeSize)
            elif direction == 'Down':
                new_rect = last_rect.move(0, -snakeSize)

            # Append the new segment
            snakeRects.append(new_rect)
            new_surf = pygame.Surface((snakeSize, snakeSize))
            new_surf.fill(green)
            snakeSurfs.append(new_surf)

    # Get key input and change direction/movement based on arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'Down':  # Prevent moving up when going down
        direction = 'Up'
        x = 0
        y = -move

    if keys[pygame.K_LEFT] and direction != 'Right':  # Prevent moving left when going right
        direction = 'Left'
        x = -move
        y = 0

    if keys[pygame.K_DOWN] and direction != 'Up':  # Prevent moving down when going up
        direction = 'Down'
        x = 0
        y = move
    if keys[pygame.K_RIGHT] and direction != 'Left':  # Prevent moving right when going left
        direction = 'Right'
        x = move
        y = 0

    # Josiah end the game when it touches itself
    for i in range(1, len(snakeRects)):
        if snakeRects[0].colliderect(snakeRects[i]):
            gameOver = True

    # Cristian: Prevent the head from going off-screen (by exiting game)
    if snakeRects[0].right < 0 or snakeRects[0].left > 750 or snakeRects[0].bottom < 0 or snakeRects[0].top > 500:
        gameOver = True

    # Fill the screen with black color to refresh the display
    screen.fill(color=black)

    # Draw grid lines on the screen every 10 pixels
    for i in range(0, 750, 10):
        pygame.draw.line(screen, blue, (i, 0), (i, 500))  # Vertical lines
    for j in range(0, 500, 10):
        pygame.draw.line(screen, blue, (0, j), (750, j))  # Horizontal lines

    # Cristian: Draw every piece of the snake
    for i in range(len(snakeRects)):
        screen.blit(snakeSurfs[i], snakeRects[i])

    # Faaris: tracks how much time has passed since game starts.
    time_passed = (pygame.time.get_ticks() - begin_ticks) // 1000
    # Faaris: displays the score text in the top right.
    score_display = game_font.render(f'Score: {score}', True, blue)
    # Faaris: displays the time text in the top right under the score.
    time_display = game_font.render(f'Time: {time_passed}s', True, blue)
    # Cristian: Display the high score text in the top right under time
    highScore_Text = game_font.render("High Score: " + str(highScore), True, blue)

    # Blit the score, time, and high score display onto the screen
    screen.blit(score_display, (10,10))
    screen.blit(time_display, (10,40))
    screen.blit(highScore_Text, (10, 70))

    screen.blit(surf2, rect2)

    # Faaris: Game over section. Cristian: Resets start position after game over and allows game to reset.
    if gameOver:
        screen.fill(black)  # Fill screen with black for game-over display

        gameOverText = game_font.render("Game Over", True, blue)
        finalScore = game_font.render("Final Score: " + str(score), True, blue)
        highScoreText = game_font.render("High Score: " + str(highScore), True, blue)
        quitText = game_font.render("Press Q to quit", True, blue)
        restartText = game_font.render("Press R to restart", True, blue)

        if score > highScore:  # Cristian: If the player has a new high score it is saved
            highScore = score
            updateScore("Score.txt", highScore)

        screen.blit(gameOverText, (250, 150))
        screen.blit(finalScore, (250, 250))
        screen.blit(highScoreText, (250, 300))
        screen.blit(restartText, (250, 350))
        screen.blit(quitText, (250, 400))

        # Cristian: If q is pressed then the game will exit
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        # Cristian: If r is pressed the game will reset and score/time will start at 0
        if keys[pygame.K_r]:
            score = 0
            gameOver = False
            snakeRects = [reset_head]
            direction = 'Right'
            counter = 1
            begin_ticks = pygame.time.get_ticks()

    # Update the display
    pygame.display.flip()
```bash
