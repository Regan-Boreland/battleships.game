from random import randint

# Legend
# @ represents ship locations
# x represents missed 
# ' ' represents available location

HIDDEN_BOARD = [[' '] * 6 for x in range(6)]
GUESS_BOARD = [[' '] * 6 for i in range(6)]

ROWS = [0, 1, 2, 3, 4, 5]
COLUMNS = [0, 1, 2, 3, 4, 5]


def display_board(board):
    print("  0 1 2 3 4 5")
    print(" -------------")
    row_number = 0
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def users_turns(number):
    row_guesses = int(input("Please pick a row (0-5): "))
    while row_guesses not in ROWS:
        print("This row doesn't exist")
        row_guesses = int(input("Please pick a row (0-5): "))
    column_guesses = int(input("Please pick a column (0-5): "))
    while column_guesses not in COLUMNS:
        print("This column doens't exist")
        column_guesses = int(input("Please pick a column (0-5): "))
    validate_users_turns()

def validate_users_turns():
    pass

def create_ships():
    pass

def count_players_hits():
    pass

def start_game():
    print("Welcome to Battleships, the ultimate guessing game")
    print("This is your board for todays game")
    display_board(GUESS_BOARD)
    print("Lets sink their ships")
    users_turns(number)

start_game()
