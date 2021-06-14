from math import inf
from time import time

# Game board and variables
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


# Function for displaying board in terminal
def display_board():
    print(f'{board[0][0]} | {board[0][1]} | {board[0][2]}')
    print(f'{board[1][0]} | {board[1][1]} | {board[1][2]}')
    print(f'{board[2][0]} | {board[2][1]} | {board[2][2]}')


# Function checks if given tile is empty (return True if space is free)
def space_is_free(x, y):
    if board[x][y] == '-':
        return True
    else:
        return False


# Function checks if board is full (return True if board is full)
def board_is_full():
    for x in board:
        for y in x:
            if y == '-':
                return False
    return True


# Check if given player won the game
def who_win(player):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == player:
        return True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == player:
        return True
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == player:
        return True
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == player:
        return True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == player:
        return True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == player:
        return True
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == player:
        return True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == player:
        return True
    else:
        return False


# Function checks if game is already drawn by someone (return True if game ended with a draw)
def draw():
    if board_is_full():
        return True
    else:
        return False


# Put given mark in a specific place on board
def make_a_move(x, y, move):
    # Check if chosen place is free
    if space_is_free(x, y):
        board[x][y] = move
        display_board()
        # Check if after that move algorithm wins
        if who_win('X'):
            print(f'AI won!')
            exit()
        # Check if after that move player wins
        elif who_win('O'):
            print(f'You won!')
            exit()
        # Check if after that move game is drawn
        elif draw():
            print(f'Game drawn')
            exit()
    # If place is full ask for making different move
    else:
        print(f"You can't choose this tile!")
        print(f"Please, choose different one!")
        x = int(input(f'Choose row! (from 1 to 3) ')) - 1
        y = int(input(f'Choose column! (from 1 to 3) ')) - 1
        make_a_move(x, y, move)


# Function for human player move
def human_move():
    x = int(input(f'Choose row! (from 1 to 3) ')) - 1
    y = int(input(f'Choose column! (from 1 to 3) ')) - 1
    make_a_move(x, y, 'O')


# Minimax function
def minimax(position, alpha, beta, turn_to_max):

    # If we reach position that ends in computer win, we return positive value
    if who_win('X'):
        return 1
    # If we reach position that ends in player win, we return negative value
    elif who_win('O'):
        return -1
    # If we reach the drawn position, we return zero
    elif draw():
        return 0

    # If that's a computer turn
    if turn_to_max:
        # We are going to compare to really small number
        best_eval = -inf

        # In loop we are trying to find first empty space
        for x in range(0, 3):
            for y in range(0, 3):
                if board[x][y] == '-':
                    # We put player mark to that position
                    position[x][y] = 'X'
                    # We start our recursive evaluation
                    eval = minimax(position, alpha, beta, False)
                    # We change position to one before evaluation
                    position[x][y] = '-'
                    # We choose bigger value as our best evaluation
                    best_eval = max(eval, best_eval)
                    # Alpha-Beta Pruning stops evaluating when next move is worse then the previous ones
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return best_eval

    # If that's a player turn
    else:
        # We are going to compare to really big number
        best_eval = inf

        # In loop we are trying to find first empty space
        for x in range(0, 3):
            for y in range(0, 3):
                if board[x][y] == '-':
                    # We put computer mark to that position
                    position[x][y] = 'O'
                    # We start our recursive evaluation
                    eval = minimax(position, alpha, beta, True)
                    # We change position to one before evaluation
                    position[x][y] = '-'
                    # We choose lesser value as our best evaluation
                    best_eval = min(eval, best_eval)
                    # Alpha-Beta Pruning stops evaluating when next move is worse then the previous ones
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return best_eval


# Function for ai player move
def ai_move():
    best_eval = -inf
    best_move_x = 0
    best_move_y = 0

    # In loop we are trying to find first empty space
    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] == '-':
                # We put player mark to that position
                board[x][y] = 'X'
                # We start our recursive evaluation
                eval = minimax(board, -inf, inf, False)
                # We change position to one before evaluation
                board[x][y] = '-'
                # We choose bigger value as our best evaluation and best position
                if eval > best_eval:
                    best_eval = eval
                    best_move_x = x
                    best_move_y = y
    # Finally, we make a move
    make_a_move(best_move_x, best_move_y, 'X')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"You start the game as 'O'")
    while True:
        start_time = time()
        ai_move()
        duration_time = time() - start_time
        print(f'Time AI took {duration_time} s to make a move')
        human_move()
        print(f'---------')
