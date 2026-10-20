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

# Initialization 
# These are all of the variables that will be used in main
pygame.init()
clock = pygame.time.Clock()
running = True
gameWon = False

board = Board()
error = ''
playerInput = ''
inputString = ''
playerTurn = 1
piecesPlaced = 0

while(running and not gameWon):
    # Display board and text to user
    board.drawBoard()                
    board.displayText(playerTurn, False)
    pygame.display.flip()
    print(error, end='')
    error = ''

    # Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playerInput = inputString 
                inputString = ''
            elif event.key == pygame.K_BACKSPACE:
                inputString = inputString[:-1]  # Remove last character
            else:
                inputString += event.unicode  # Add the pressed key to the input

    # If the string is empty restart loop
    if (playerInput == ''):
        continue
    elif (playerInput == 'q'):
        running = False
        continue

    # Check if user input a valid column number
    try:
        num = int(playerInput)
    except:
        error = "Invalid input"
        continue

    # Place piece on board
    result = board.placePiece(num, playerTurn)

    # Reset user input
    playerInput = ''

    # Column was full
    if (result == -2):
        error = "Column " + str(playerInput) + " is full"
    # Column was out of range
    elif (result == -1):
        error = str(playerInput) + " is not a valid column"
    # Placement was successful
    elif (result == 0): 
        if (playerTurn == 1):
            playerTurn = 2
        else:
            playerTurn = 1
        piecesPlaced += 1
        if (piecesPlaced >= NUM_COLS * NUM_ROWS):
            board.drawBoard()
            board.displayText(0, True)
            pygame.display.flip()
            gameWon = True
    # Current player won
    else:
        board.drawBoard()
        board.displayText(playerTurn, True)
        pygame.display.flip()
        gameWon = True

    clock.tick(FPS)

# Display board until user quits
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

# Exit the program
pygame.quit()
exit()