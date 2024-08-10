from typing import List
from IPython.display import clear_output
import random

# Display the board
def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

# Assign players a marker
def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input('Player 1: Please Pick X or O:\n').upper()
    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'
    print(f'Player 1: you are {player1}')
    print(f'Player 2: you are {player2}')
    return player1, player2

# Place the marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# Check board for 3 marks in a row
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or # Across middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or # Across bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or # Down the left
            (board[2] == mark and board[5] == mark and board[8] == mark) or # Down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or # Down right
            (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark)) # Diagonal

# Decide who goes first
def choose_first():
    return random.choice([1, 2])

# Check if spot is free on the board
def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Player's choice of position
def player_choice(board):
    while True:
        try:
            position = int(input('Choose your next position: (1-9) '))
            if position in range(1, 10) and space_check(board, position):
                return position
            else:
                print("Position is either occupied or invalid. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Replay the game
def replay():
    return input('Do you want to play again? Yes or No? \n').lower().startswith('y')

# Greeting
print("Hello, Let's play Tic-Tac-Toe!\n")

# Set up the game
while True:
    theBoard = [" "] * 10
    player1, player2 = player_input()
    turn = choose_first()
    print(f"{'Player 1' if turn == 1 else 'Player 2'} will go first.")

    play_game = input('Are you ready to play? Y or N?\n')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1's turn
        if turn == 1:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1, position)

            if win_check(theBoard, player1):
                display_board(theBoard)
                print("Congrats Player 1! You WIN!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a DRAW!")
                    break
                else:
                    turn = 2
        # Player 2's turn
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2, position)

            if win_check(theBoard, player2):
                display_board(theBoard)
                print("Congrats Player 2! You WIN!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a DRAW!")
                    break
                else:
                    turn = 1

    if not replay():
        break

