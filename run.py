from random import randint

# Legend
# @ represents ship locations
# x represents missed 
# ' ' represents available location
# # represents hit ship

HIDDEN_BOARD = [[' '] * 6 for x in range(6)]
GUESS_BOARD = [[' '] * 6 for i in range(6)]

ROWS = [0, 1, 2, 3, 4, 5]
COLUMNS = [0, 1, 2, 3, 4, 5]

row = ""
column = ""

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
    global row_guess
    while True:
        try:
            row_guess = int(input("Pick a row (between 0-5): "))
            if row_guess in ROWS:
                break 
        except ValueError:
            print("Please enter a row on the board")
    #validation for column guess
    global column_guess
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

points = 0

def increment_points(board):
    """
    increases players points if a ship is hit
    """
    #global points
    #points = 0
    # searches the hidden board and if players guess aligns with ship location then increase points by one
    for row_guess in board:
        for column_guess in row_guess:
            if column_guess == '@':
                points += 1
    #return points

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
    display_board(HIDDEN_BOARD)
    turns = 10
    points = 0
    while turns > 0:
        users_turn(input)
        #adds symbols to guess and hidden board based on user input
        if GUESS_BOARD[row_guess][column_guess] == 'X':
            print("You've already used those coordinates, pick again")
        elif HIDDEN_BOARD[row_guess][column_guess] == '@':
            print("Good job commander, you sunk their ship")
            GUESS_BOARD[row_guess][column_guess] = '#'
            turns -= 1
            print(f"You have {turns} lives remaining")
        else:
            print("You missed! Focus and sink their ships")
            GUESS_BOARD[row_guess][column_guess] = 'X'
            turns -=1
            print(f"you have {turns} lives remaining")
        if GUESS_BOARD[row_guess][column_guess] == '#':
            points += 1 
            print(f"You have sunk {points} ships")
        if points == 4:
            print("There's only one target left")
            print("Hurry up and end this before we're out of ammunition")
        #ends the game when points reach 5 or turns reach 0
        if points == 5:
            print("Congratulations you sunk all their ships")
            print("GAME OVER!!!")
            break
        if turns == 0:
            print("Wer're out of ammunition\nWe'll get them next time")
        display_board(GUESS_BOARD)

start_game()