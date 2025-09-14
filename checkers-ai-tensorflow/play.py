# play.py
# Command-line interface to play Checkers vs AI

import numpy as np
import tensorflow as tf
from checkers_ai import initial_board, flatten_board, predict_move, BOARD_SIZE
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Load trained model
model = tf.keras.models.load_model("checkers_ai_model.h5")

def render(board):
    print("\n   " + "  ".join([str(i) for i in range(BOARD_SIZE)]))
    for i, row in enumerate(board):
        display_row = []
        for j, cell in enumerate(row):
            is_dark = (i + j) % 2 == 1
            bg = Back.BLACK if is_dark else Back.RESET
            if cell == 1:
                fg = Fore.RED
                symbol = "O"
            elif cell == -1:
                fg = Fore.BLUE
                symbol = "X"
            elif cell == 2:
                fg = Fore.YELLOW
                symbol = "O"
            elif cell == -2:
                fg = Fore.YELLOW
                symbol = "X"
            else:
                fg = Fore.RESET
                symbol = " "
            display_row.append(fg + bg + f" {symbol} " + Style.RESET_ALL)
        print(f"{i} " + "".join(display_row))

def player_move(board):
    try:
        row = int(input("Enter row of piece to move: "))
        col = int(input("Enter column of piece to move: "))
        while True:
            new_row = int(input("Enter new row: "))
            new_col = int(input("Enter new column: "))

            # Capture move
            if abs(new_row - row) == 2 and abs(new_col - col) == 2:
                mid_r = (row + new_row) // 2
                mid_c = (col + new_col) // 2
                if board[row][col] == 1 and board[new_row][new_col] == 0 and board[mid_r][mid_c] == -1:
                    board[mid_r][mid_c] = 0
                    board[row][col] = 0
                    if new_row == BOARD_SIZE - 1:
                        board[new_row][new_col] = 2
                        print("Your piece has been kinged!")
                    else:
                        board[new_row][new_col] = 1
                    print(f"You captured at ({mid_r}, {mid_c})!")
                    row, col = new_row, new_col

                    more_jumps = False
                    for dr, dc in [(1, -1), (1, 1)]:
                        r2, c2 = row + 2*dr, col + 2*dc
                        mr, mc = row + dr, col + dc
                        if (
                            0 <= r2 < BOARD_SIZE and
                            0 <= c2 < BOARD_SIZE and
                            board[r2][c2] == 0 and
                            board[mr][mc] == -1
                        ):
                            more_jumps = True
                            break

                    if not more_jumps:
                        return
                    else:
                        print("You have another jump!")
                        continue

            # Normal move
            elif abs(new_row - row) == 1 and abs(new_col - col) == 1:
                piece = board[row][col]
                if piece in [1, 2] and board[new_row][new_col] == 0:
                    if piece == 1 and new_row != BOARD_SIZE - 1:
                        board[new_row][new_col] = 1
                    elif piece == 1 and new_row == BOARD_SIZE - 1:
                        board[new_row][new_col] = 2
                        print("Your piece has been kinged!")
                    elif piece == 2:
                        board[new_row][new_col] = 2  # King stays king
                    board[row][col] = 0
                    return

            print("Invalid move. Try again.")
    except:
        print("Invalid input. Try again.")

def ai_move(board):
    # Look for the best initial jump
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] in [-1, -2]:
                piece = board[r][c]
                directions = [(-1, -1), (-1, 1)] if piece == -1 else [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dr, dc in directions:
                    mid_r, mid_c = r + dr, c + dc
                    end_r, end_c = r + 2*dr, c + 2*dc
                    if (
                        0 <= end_r < BOARD_SIZE and
                        0 <= end_c < BOARD_SIZE and
                        board[mid_r][mid_c] in [1, 2] and
                        board[end_r][end_c] == 0
                    ):
                        board[r][c] = 0
                        board[mid_r][mid_c] = 0
                        if end_r == 0:
                            board[end_r][end_c] = -2
                            print("AI piece promoted to king!")
                        else:
                            board[end_r][end_c] = piece
                        print(f"AI captures from ({r}, {c}) to ({end_r}, {end_c}) over ({mid_r}, {mid_c})")
                        r, c = end_r, end_c

                        # Chain jumps
                        while True:
                            jumped = False
                            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                            for dr2, dc2 in directions:
                                mr, mc = r + dr2, c + dc2
                                nr, nc = r + 2*dr2, c + 2*dc2
                                if (
                                    0 <= nr < BOARD_SIZE and
                                    0 <= nc < BOARD_SIZE and
                                    board[mr][mc] in [1, 2] and
                                    board[nr][nc] == 0
                                ):
                                    board[mr][mc] = 0
                                    board[r][c] = 0
                                    if nr == 0:
                                        board[nr][nc] = -2
                                        print("AI piece promoted to king!")
                                    else:
                                        board[nr][nc] = piece
                                    print(f"AI continues jump to ({nr}, {nc}) over ({mr}, {mc})")
                                    r, c = nr, nc
                                    jumped = True
                                    break
                            if not jumped:
                                return
                        return

    # Regular move
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] in [-1, -2]:
                piece = board[r][c]
                directions = [(-1, -1), (-1, 1)] if piece == -1 else [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == 0:
                        board[r][c] = 0
                        if nr == 0:
                            board[nr][nc] = -2
                            print("AI piece promoted to king!")
                        else:
                            board[nr][nc] = piece
                        print(f"AI moves from ({r}, {c}) to ({nr}, {nc})")
                        return

    print("AI has no valid moves!")

    # Regular move
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] in [-1, -2]:
                for dr, dc in [(-1, -1), (-1, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == 0:
                        board[r][c] = 0
                        if nr == 0:
                            board[nr][nc] = -2
                            print("AI piece promoted to king!")
                        else:
                            board[nr][nc] = -1
                        print(f"AI moves from ({r}, {c}) to ({nr}, {nc})")
                        return

    print("AI has no valid moves!")

def check_game_over(board):
    player_pieces = sum(cell in [1, 2] for row in board for cell in row)
    ai_pieces = sum(cell in [-1, -2] for row in board for cell in row)

    if player_pieces == 0:
        render(board)
        print(Fore.CYAN + "\nYou lost. Game Over!")
        return True
    elif ai_pieces == 0:
        render(board)
        print(Fore.CYAN + "\nYou win! Game Over!")
        return True
    return False

if __name__ == "__main__":
    # Hardcoded board for final move scenario
    board = [[None for _ in range(8)] for _ in range(8)]

    # Place AI's last piece
    board[2][3] = {'row': 2, 'col': 3, 'color': 'x', 'king': False}

    # Place user's piece that can jump and win
    board[3][2] = {'row': 3, 'col': 2, 'color': 'o', 'king': False}

    while True:
        render(board)
        player_move(board)
        if check_game_over(board):
            print("Game Over! Player wins!")
            break
        render(board)
        ai_move(board)
        if check_game_over(board):
            print("Game Over! AI wins!")
            break



