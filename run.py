from random import randint


"""
The first board is for displaying the ship locations and it is hidden
while the second is for diplaying player guesses and is shown
"""
RANDOM_BOARD = []
for x in range(6):
    RANDOM_BOARD.append([" "] * 6)
PLAYER_BOARD = []
for x in range(6):
    PLAYER_BOARD.append([" "] * 6)

print("******WELCOME TO FUNTIME BATTLESHIPS******\n")


def show_board(board):
    """
    Displays the board for guesses
    """
    print("=================================")
    print("Guess a row and column to hit")
    print("Row Guess: 1-6, Column Guess: A-F")
    print("=================================")
    print("X = Hit, - = Miss\n")
    print("  A B C D E F")
    print("  #-#-#-#-#-#")

    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


alpha_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}


def create_ships(board):
    """
    creates 3 random ship on the hidden board and check to avoid
    placing ships on the sma spot
    """
    for i in range(3):
        ship_row, ship_col = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 5), randint(0, 5)
        board[ship_row][ship_col] = "X"


def player_ship_location():
    """
    Collects player row and column guesses and validates if they
    are the required data.
    """
    row = input("Guess a Row: ")
    while row not in "123456":
        print("Invalid Row. Guess should be between 1-6")
        row = input("Guess a Row: ")
    col = input("Guess a Col: ").upper()
    while col not in "ABCDEF":
        print("Invalid Column. Guess should be between A-F")
        col = input("Guess a Col: ").upper()
    return int(row) - 1, alpha_to_num[col]


def count_ships(board):
    """
    Counts the number of hits and check if it is equal
    to 3 within the allowed turns.
    """
    count = 0
    for row in board:
        for col in row:
            if col == "X":
                count += 1
    return count


create_ships(RANDOM_BOARD)
turns = 6
while turns > 0:
    show_board(PLAYER_BOARD)
    row, col = player_ship_location()
    if PLAYER_BOARD[row][col] == "-" or PLAYER_BOARD[row][col] == "X":
        print("Already guessed. Make a new guess")
    elif RANDOM_BOARD[row][col] == "X":
        print("Hurray! It's a HIT")
        PLAYER_BOARD[row][col] = "X"
        turns -= 1
    else:
        print("Sorry, It's a MISS!")
        PLAYER_BOARD[row][col] = "-"
        turns -= 1
    if count_ships(PLAYER_BOARD) == 3:
        print("You win!")
        print("Congratulations! You've sunk the ship")
        break
    print(f"You have {turns} turns left\n")
    if turns == 0:
        print("You ran out of turns")
        print("GAME OVER")
