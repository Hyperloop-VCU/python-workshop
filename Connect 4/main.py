from board import *

class Game:
    def __init__(self):
        self.board = Board()
        self.error = ''
        self.playerTurn = 1
        self.piecesPlaced = 0

    def run(self):
        while(1):
            # Print board
            self.board.printBoard()
            print("\n")

            # Print error if applicable
            if (self.error != ''):
                print(self.error)
                
            # Print options
            print("Input 1-7 to place your piece\nInput 'q' to quit\n")

            # Print player turn
            if (self.playerTurn == 1):
                print(RED_TEXT + "Player " + str(self.playerTurn) + "'s turn" + RESET + "\nInput: ", end='')
            elif (self.playerTurn == 2):
                print(YELLOW_TEXT + "Player " + str(self.playerTurn) + "'s turn" + RESET + "\nInput: ", end='')
            else:
                self.error = "Invalid player number"
                break

            # Get input
            self.playerInput = input()

            # Clear screen
            print(CLEAR_SCREEN, end='')

            if (self.playerInput == 'q'):
                break

            # Check if user input a valid column number
            try:
                num = int(self.playerInput)
            except:
                self.error = "Invalid input"
                continue

            result = self.board.placePiece(num, self.playerTurn)
            if (result == -2):
                self.error = "Column " + self.playerInput + " is full"
            elif (result == -1):
                self.error = self.playerInput + " is not a valid column"
            elif (result == 0):
                if (self.playerTurn == 1):
                    self.playerTurn = 2
                else:
                    self.playerTurn = 1
                self.piecesPlaced += 1
                if (self.piecesPlaced >= NUM_COLS * NUM_ROWS):
                    # Game is a draw
                    self.board.printBoard()
                    print("\n\nGame is a draw")
                    break
            else:
                # Current player won
                self.board.printBoard()
                print("\n\n")
                if (self.playerTurn == 1):
                    print(RED_TEXT + BOLD_TEXT + "Player 1 wins" + RESET)
                elif (self.playerTurn == 2):
                    print(YELLOW_TEXT + BOLD_TEXT + "Player 2 wins!" + RESET)
                break

if __name__ == '__main__':
    game = Game()
    game.run()