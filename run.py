from random import randint


"""
BOARD_1 is for displaying the ship locations and it is hidden
while BOARD_2 is for diplaying player guesses and is shown
"""
BOARD_1 = []
for x in range(6):
    BOARD_1.append([" "] * 6)
BOARD_2 = []
for x in range(6):
    BOARD_2.append([" "] * 6)

print("******WELCOME TO BATTLESHIP******\n")


def show_board(board):
    """
    Displays the board for guesses
    """
    print("=================================")
    print("Guess a row and column to hit")
    print("Row must be between 1-6")
    print("Column must be between A-F")
    print("=================================")
    print("X = Hit, - = Miss\n")
    print("  A B C D E F")
    print("  #-#-#-#-#-#")
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

alpha_to_num = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5,}


def create_ships(board):
    """
    creates 3 random ship on the hidden board and check to avoid
    placing ships on the sma spot
    """
    for x in range(3):
        ship_row, ship_col = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 5), randint(0, 5)
        board[ship_row][ship_col] = "X"

