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

def users_turn(input):
    #validation for row guess
    while True:
        try:
            row_guess = int(input("Pick a row (between 0-5): "))
            if row_guess in ROWS:
                break
        except ValueError:
            print("Please enter a row on the board")
    #validation for column guess
    while True:
        try:
            column_guess = int(input("Pick a column (between 0-5): "))
            if column_guess in COLUMNS:
                break
        except ValueError:
            print("Please enter a column on the board")

def create_ships(board):
    """
    creates the ships locations on the hidden board
    if the location already has a ship then the computer places a ship elsewhere
    """
    for ship in range(5):
        ship_row = randint(0,5)
        ship_column = randint(0,5)
        #uses randint to find a location on the board for a ship,
        #if a location is already taken then run again till a location is found
        if board[ship_row] [ship_column] == '@':
            ship_row, ship_column = randint(0,5), randint(0,5)
        else:
            board[ship_row][ship_column] = '@'

def count_players_hits():
    """
    increases players points if a ship is hit
    """
    points = 0
    # searches the hidden board and if players guess aligns with ship location then increase points by one
    for row_guess in board:
        for column_guess in row_guess:
            if column_guess == '@':
                points += 1
    return points

def start_game():
    """
    starts the game
    """
    print("Welcome to Battleships, the ultimate guessing game")
    print("--------------------------------------------------")
    print("Our game works a little different to a normal game,\nrather than playing against someone you will be given 10 lives,\nyou have to hit the 5 boats within the 10 lives\nor it's GAME OVER")
    print("--------------------------------------------------")
    print("This is your board for todays game")
    display_board(GUESS_BOARD)
    print("LETS SINK THEIR SHIPS!!!")
    create_ships(HIDDEN_BOARD)
    users_turn(input)

start_game()