from random import randint

# Legend
# @ represents ship locations
# x represents missed 
# ' ' represents available location

HIDDEN_BOARD = [[''] * 5 for x in range(5)]
GUESS_BOARD = [[''] * 5 for x in range(5)]

ROWS = [0, 1, 2, 3, 4]
COLUMNS = [0, 1, 2, 3, 4]

def start_game():
    pass

def display_board():
    print("  0 1 2 3 4")
    print("  ---------")

display_board()

def users_turn():
    pass

def validate_users_turn():
    pass

def create_ships():
    pass

def count_players_hits():
    pass