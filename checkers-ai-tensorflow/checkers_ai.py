import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

BOARD_SIZE = 8

# 0 = empty, 1 = player piece, 2 = player king, -1 = AI piece, -2 = AI king
def initial_board():
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    for row in range(3):
        for col in range((row + 1) % 2, BOARD_SIZE, 2):
            board[row][col] = 1
    for row in range(5, 8):
        for col in range((row + 1) % 2, BOARD_SIZE, 2):
            board[row][col] = -1
    return board

def flatten_board(board):
    return board.flatten()

def dummy_data(num_samples=1000):
    X = []
    y = []
    for _ in range(num_samples):
        board = initial_board()
        X.append(flatten_board(board))
        move = np.random.randint(0, BOARD_SIZE * BOARD_SIZE)  # Simplified move index
        y.append(tf.keras.utils.to_categorical(move, BOARD_SIZE * BOARD_SIZE))
    return np.array(X), np.array(y)

def build_model():
    model = Sequential([
        Flatten(input_shape=(BOARD_SIZE * BOARD_SIZE,)),
        Dense(128, activation='relu'),
        Dense(128, activation='relu'),
        Dense(BOARD_SIZE * BOARD_SIZE, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train():
    X, y = dummy_data()
    model = build_model()
    model.fit(X, y, epochs=10, batch_size=32)
    model.save("checkers_ai_model.h5")
    print("Model trained and saved as 'checkers_ai_model.h5'")

def predict_move(model, board):
    flat = flatten_board(board).reshape(1, -1)
    prediction = model.predict(flat, verbose=0)[0]
    return np.argmax(prediction)  # index of best move

if __name__ == "__main__":
    train()
