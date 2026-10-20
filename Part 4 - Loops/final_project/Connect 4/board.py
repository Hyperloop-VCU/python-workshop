""" Connect 4

In this file is all of the code to manage the screen and the board logic

IDEAS
- Change the number of columns and rows
- Change the amount needed in a row to win
- Change the screen size
- Change the size of the circles
- Add column number indicators
- Change what text is displayed
- Change the color and font of the text

"""

import pygame

# Colors for the board
BACKGROUND = (18, 18, 28)
BOARD_COLOR = (47, 52, 179)
RED_COLOR = (247, 59, 42)
YELLOW_COLOR = (252, 252, 39)
LIT_COLOR = (255, 255, 255)
TEXT_COLOR = (240, 240, 245)
DIM_TEXT_COLOR = (150, 150, 165)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 600

# Size of board
NUM_ROWS = 6
NUM_COLS = 7
# Number in a row to win
NUM_IN_A_ROW = 4

class Board:
    def __init__(self):
        # Create board
        self.board = list()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Connect 4")
        self.win_font = pygame.font.SysFont("arial", 44, bold=True)
        self.text_font = pygame.font.SysFont("arial", 26)
        for i in range(NUM_COLS):
            self.board.append(list())

    def placePiece(self, column, player):
        # Return if column out of bounds
        if (column > NUM_COLS or column < 1):
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
            if (column + i >= NUM_COLS or self.top - i < 0):
                break
            elif (self.top - i >= len(self.board[column + i])):
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
            if (column - i < 0 or self.top - i < 0):
                break
            elif (self.top - 1 >= len(self.board[column - i])):
                break
            if (self.board[column - i][self.top - i] != player):
                break
            self.pieceCount += 1
        # Check if player won in this direction
        if (self.pieceCount >= 4):
            return player

        # Player did not win
        return 0

    def drawBoard(self):
        self.screen.fill(BACKGROUND)
        pygame.draw.rect(self.screen, BOARD_COLOR, (90, 40, 540, 460))

        xOffset = 500 / NUM_COLS
        yOffset = 420 / NUM_ROWS

        radius = (xOffset if xOffset < yOffset else yOffset) * 0.45

        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                cellX = radius + 110 + i * xOffset
                cellY = radius + 60 + j * yOffset
                if (j >= len(self.board[i])):
                    pygame.draw.circle(self.screen, BACKGROUND, (cellX, cellY), radius)
                    continue
                player = self.board[i][j]
                if (player == 1):
                    pygame.draw.circle(self.screen, RED_COLOR, (cellX, cellY), radius)
                elif (player == 2):
                    pygame.draw.circle(self.screen, YELLOW_COLOR, (cellX, cellY), radius)

    # Player is the current players turn
    # Error is the error to display if any
    # playerWin is true if a player won
    def displayText(self, player, playerWin):
        if (playerWin):
            if (player == 1):
                winLabel = self.win_font.render("Player 1 wins!", True, RED_COLOR)
            elif (player == 2):
                winLabel = self.win_font.render("Player 2 wins!", True, YELLOW_COLOR)
            else:
                winLabel = self.win_font.render("Game is a draw!", True, TEXT_COLOR)
            
            winLabelRect = winLabel.get_rect()
            winLabelRect.center = (SCREEN_WIDTH / 2, 530)
            self.screen.blit(winLabel, winLabelRect)
            return

        if (player == 1):
            turnLabel = self.text_font.render("Player 1's turn", True, RED_COLOR)
        else:
            turnLabel = self.text_font.render("Player 2's turn", True, YELLOW_COLOR)
        turnLabelRect = turnLabel.get_rect()
        turnLabelRect.center = (SCREEN_WIDTH / 2, 580)
        self.screen.blit(turnLabel, turnLabelRect)

        info1Label = self.text_font.render("Input a column number or 'q' to quit", True, DIM_TEXT_COLOR)
        info1LabelRect = info1Label.get_rect()
        info1LabelRect.center = (SCREEN_WIDTH / 2, 525)
        self.screen.blit(info1Label, info1LabelRect)

        info2Label = self.text_font.render("Press enter when done", True, DIM_TEXT_COLOR)
        info2LabelRect = info2Label.get_rect()
        info2LabelRect.center = (SCREEN_WIDTH / 2, 550)
        self.screen.blit(info2Label, info2LabelRect)