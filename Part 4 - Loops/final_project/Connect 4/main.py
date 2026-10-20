""" Connect 4

This is the classic game Connect 4

In this file is all of the code to manage timing and user input

IDEAS
- To send the input to the program, instead of pressing 'enter', the user presses 'space'
- Make it so the game never ends
- Make it so the player places a piece in a random position whenever they play
"""

import pygame
from board import *

FPS = 60

class Game:
    # Initialization function for Game
    # This function will run once when Game is first created / Program is first run
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.gameWon = False

        self.board = Board()
        self.error = ''
        self.playerInput = ''
        self.inputString = ''
        self.playerTurn = 1
        self.piecesPlaced = 0

    def run(self):
        while(self.running and not self.gameWon):
            # Displat board and text to user
            self.board.drawBoard()                
            self.board.displayText(self.playerTurn, False)
            pygame.display.flip()

            # Get user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.playerInput = self.inputString 
                        self.inputString = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.inputString = self.inputString[:-1]  # Remove last character
                    else:
                        self.inputString += event.unicode  # Add the pressed key to the input

            # If the string is empty restart loop
            if (self.playerInput == ''):
                continue
            elif (self.playerInput == 'q'):
                self.running = False
                continue

            # Check if user input a valid column number
            try:
                num = int(self.playerInput)
            except:
                self.error = "Invalid input"
                continue

            # Place piece on board
            result = self.board.placePiece(num, self.playerTurn)

            # Reset user input
            self.playerInput = ''

            # Column was full
            if (result == -2):
                self.error = "Column " + str(self.playerInput) + " is full"
            # Column was out of range
            elif (result == -1):
                self.error = str(self.playerInput) + " is not a valid column"
            # Placement was successful
            elif (result == 0): 
                if (self.playerTurn == 1):
                    self.playerTurn = 2
                else:
                    self.playerTurn = 1
                self.piecesPlaced += 1
                if (self.piecesPlaced >= NUM_COLS * NUM_ROWS):
                    self.board.drawBoard()
                    self.board.displayText(0, True)
                    pygame.display.flip()
                    self.gameWon = True
            # Current player won
            else:
                self.board.drawBoard()
                self.board.displayText(self.playerTurn, True)
                pygame.display.flip()
                self.gameWon = True

            print(self.error, end='')
            self.clock.tick(FPS)

        # Display board until user quits
        while (self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False

if __name__ == '__main__':
    game = Game()
    game.run()
    exit()
