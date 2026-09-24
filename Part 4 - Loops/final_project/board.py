# Put this in print to make it colored text
RED_TEXT     = "\x1b[0;31m"
YELLOW_TEXT  = "\x1b[0;33m"
RED_BACK     = "\x1b[0;41m"
YELLOW_BACK  = "\x1b[0;43m"
WHITE_BACK   = "\x1b[0;47m"
RESET        = "\x1b[0m"
CLEAR_SCREEN = "\x1b[2J\x1b[1;1H"
BOLD_TEXT    = "\x1b[1m"

# Size of board
NUM_ROWS = 6
NUM_COLS = 7
# Number in a row to win
NUM_IN_A_ROW = 4


class Board:
    def __init__(self):
        # Create board
        self.board = list()
        for i in range(NUM_COLS):
            self.board.append(list())

    def placePiece(self, column, player):
        # Return if column out of bounds
        if (column > NUM_COLS | column < 1):
            return -1
        # Return if column is full
        if (len(self.board[column - 1]) >= NUM_ROWS):
            return -2
        # Add piece to board
        self.board[column - 1].append(player)
        # Check if player won
        return self.checkWinner(column - 1, player)

    def checkWinner(self, column, player):
        # Get the row the last piece was placed
        self.top = len(self.board[column]) - 1

        self.pieceCount = 1
        # ----------------------- Check down
        for i in range(1,4):
            if (self.top - i < 0):
                break
            if (self.board[column][self.top - i] != player):
                break
            self.pieceCount += 1
        # Check if player won in this direction
        if (self.pieceCount >= 4):
            return player

        self.pieceCount = 1
        # ----------------------- Check left
        for i in range(1,4):
            if (column - i < 0):
                break
            elif (self.top >= len(self.board[column - i])):
                break
            if (self.board[column - i][self.top] != player):
                break
            self.pieceCount += 1
        # ----------------------- Check right
        for i in range(1,4):
            if (column + i >= NUM_COLS):
                break
            elif (self.top >= len(self.board[column + i])):
                break
            if (self.board[column + i][self.top] != player):
                break
            self.pieceCount += 1
        # Check if player won in this direction
        if (self.pieceCount >= 4):
            return player

        self.pieceCount = 1
        # ----------------------- Check up left
        for i in range(1,4):
            if (column - i < 0):
                break
            elif (self.top + i >= len(self.board[column - i])):
                break
            if (self.board[column - i][self.top + i] != player):
                break
            self.pieceCount += 1
        # ----------------------- Check down right
        for i in range(1,4):
            if (column + i >= NUM_COLS | self.top - i < 0):
                break
            elif (self.top >= len(self.board[column + i])):
                break
            if (self.board[column + i][self.top - i] != player):
                break
            self.pieceCount += 1
        # Check if player won in this direction
        if (self.pieceCount >= 4):
            return player

        self.pieceCount = 1
        # ----------------------- Check up right
        for i in range(1,4):
            if (column + i >= NUM_COLS):
                break
            elif (self.top + i >= len(self.board[column + i])):
                break
            if (self.board[column + i][self.top + i] != player):
                break
            self.pieceCount += 1
        # ----------------------- Check down left
        for i in range(1,4):
            if (column - i < 0 | self.top - i < 0):
                break
            elif (self.top >= len(self.board[column - i])):
                break
            if (self.board[column - i][self.top - i] != player):
                break
            self.pieceCount += 1
        # Check if player won in this direction
        if (self.pieceCount >= 4):
            return player

        # Player did not win
        return 0

    def printBoard(self):
        # Print all rows
        for i in range(NUM_ROWS -1, -1, -1):

            # Print left side of board
            print_white_square(newline=False)

            # Print pieces and dividers
            for j in range(NUM_COLS * 2 - 1):
                if (j % 2 == 1):
                    print("|", end='')
                else:
                    # Print colored 'O' based off of which player is in spot
                    if (i < len(self.board[int(j/2)])):
                        if (self.board[int(j/2)][i] == 1):
                            fancy_print("O", color="red", newline=False)
                        elif (self.board[int(j/2)][i] == 2):
                            fancy_print("O", color="yellow", newline=False)
                        else:
                            print(" ", end='')
                    else:
                        print(" ", end='')
            
            # Print right side of board
            print_white_square(newline=True)

        # Print bottom of board
        for i in range(NUM_COLS * 2 + 1):
            print_white_square(newline=False)
        print()



def fancy_print(text, bold=False, color="white", newline=True):
    settings = RESET

    if color == "red":
        settings += RED_TEXT
    elif color == "yellow":
        settings += YELLOW_TEXT 
    if bold:
        settings += BOLD_TEXT

    if not newline:
        print(settings + text + RESET, end='')
    else:
        print(settings + text + RESET)

def print_white_square(newline=True):
    if newline:
        print(WHITE_BACK + " " + RESET)
    else:
        print(WHITE_BACK + " " + RESET, end='')