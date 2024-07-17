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
    """
    displays the board to the player
    """
    print("  0 1 2 3 4 5")
    print(" -------------")
    row_number = 0
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def users_turns(input):
    """
    requests players guess on a row and column
    """
    row_guesses = int(input("Please pick a row (0-5): "))
    while row_guesses not in ROWS:
        print("This row doesn't exist")
        row_guesses = int(input("Please pick a row (0-5): "))
    column_guesses = int(input("Please pick a column (0-5): "))
    while column_guesses not in COLUMNS:
        print("This column doens't exist")
        column_guesses = int(input("Please pick a column (0-5): "))
    return ROWS[row_guesses], COLUMNS[column_guesses]

def create_ships(board):
    """
    creates the ships locations on the hidden board
    if the location already has a ship then the computer places a ship elsewhere
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,5), randint(0,5)
        if board[ship_row] [ship_column] == '@':
            ship_row, ship_column = randint(0,5), randint(0,5)
        else:
            board[ship_row][ship_column] = '@'

#increases the points counter if player hits the ship
def count_players_hits():
    pass


def start_game():
    """
    starts the game
    """
    print("Welcome to Battleships, the ultimate guessing game")
    print("Todays board is a little different to normal, we're using zero index so the top left corner will be 0,0\nand the bottom right will be 5,5")
    print("This is your board for todays game")
    display_board(GUESS_BOARD)
    print("Lets sink their ships")
    create_ships(HIDDEN_BOARD)
    users_turns(input)


