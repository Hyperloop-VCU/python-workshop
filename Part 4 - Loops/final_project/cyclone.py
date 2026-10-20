""" 3.x - CYCLONE

This is that classic "stop the light on the jackpot" arcade game, written in python.
This is your chance to mess around and have fun!


IDEAS
- Remove all the bad prizes
- Remove all the good prizes
- Make the cursor move faster / slower
- Add more prizes
- Change the background / prize colors
- Make the circles bigger / smaller

- Make an additional cursor that spins slower than the first one
- If you press "r", the score and round count reset
- If you press "x", all the prize values are randomized
- If you press "a", a new random prize is added
- If you press "d", a prize is deleted
- Add a "danger prize" - if that one is hit, show a "game over" screen
- Make the cursor change speed randomly
- Make the cursor speed depend on its position or speed up / slow down over time
- Use the arrow keys to change cursor speed
- If you hit the highest prize 3 times in a row, show a "you win" screen
- Tell the player to get a life if they play more than 10 rounds

"""

import pygame
import math
import random # to get a random integer between x and y, use random.randint(x, y)

# -- Settings --
PRIZES = [100, 50, 200, 50, 500, 50, 100, -1000, 1000, 50, 100, 50, 200, 50, -500, 50]

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 600

FRAMES_PER_STEP = 3
FPS = 60

CENTER_X = 360        # the middle of the ring
CENTER_Y = 290
RING_RADIUS = 180     # how far the cells sit from the middle
CELL_RADIUS = 30      # how big each cell is

# Colors (red, green, blue)
BACKGROUND = (18, 18, 28)
LIT_COLOR = (255, 255, 255)
TEXT_COLOR = (240, 240, 245)
DIM_TEXT_COLOR = (150, 150, 165)


# -- Setup --
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyclone")
clock = pygame.time.Clock()
bigFont = pygame.font.SysFont("arial", 44, bold=True)
font = pygame.font.SysFont("arial", 26)
smallFont = pygame.font.SysFont("arial", 22, bold=True)

# -- Define function for mapping prize values to colors --
def get_color(value):
    gray = (128, 128, 128)
    red = (200, 20, 20)
    gold = (255, 200, 0) 

    if value < -1000:
        value = -1000
    if value > 1000:
        value = 1000

    if value < 0:
        target = red
    else:
        target = gold

    amount = abs(value) / 1000

    r = gray[0] + (target[0] - gray[0]) * amount
    g = gray[1] + (target[1] - gray[1]) * amount
    b = gray[2] + (target[2] - gray[2]) * amount
    return (round(r), round(g), round(b))


# -- Define functions for drawing stuff on the screen --
def get_screen_position_of_cell(index):
    sliceAngle = (2 * math.pi) / len(PRIZES)
    angle = (index * sliceAngle) - (math.pi / 2)   # start at the top of the ring
    x = CENTER_X + (RING_RADIUS * math.cos(angle))
    y = CENTER_Y + (RING_RADIUS * math.sin(angle))
    return int(x), int(y)

def draw_cell(index, isLit):
    prize = PRIZES[index]
    cellX, cellY = get_screen_position_of_cell(index)

    # pick the color
    color = get_color(prize)

    if isLit:
        color = LIT_COLOR

    pygame.draw.circle(screen, color, (cellX, cellY), CELL_RADIUS)

    # the prize number, centered inside the circle
    if isLit:
        label = smallFont.render(str(prize), True, BACKGROUND)
    else:
        label = smallFont.render(str(prize), True, TEXT_COLOR)
    labelRect = label.get_rect()
    labelRect.center = (cellX, cellY)
    screen.blit(label, labelRect)

def draw_ring(pointer):
    for index in range(len(PRIZES)):
        if index == pointer:
            draw_cell(index, True)
        else:
            draw_cell(index, False)


def draw_centered_text(message, y, whichFont, color):
    label = whichFont.render(message, True, color)
    labelRect = label.get_rect()
    labelRect.center = (SCREEN_WIDTH / 2, y)
    screen.blit(label, labelRect)

def is_space_pressed():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return True
    return False


# -- Game state --
pointer = 0          # which cell is lit right now
cursor_moving = True      # is the light moving?
lastPrize = 0        # what the player won on the most recent round
totalScore = 0       # accumulation of all the prizes won over all rounds
roundNumber = 1      # round number
frameCount = 0       # keeps track of how many frames have passed

def draw_game():
    screen.fill(BACKGROUND)
    draw_ring(pointer)
    
    draw_centered_text("CYCLONE", 38, bigFont, TEXT_COLOR)
    
    # the middle of the ring: score, or the prize just won
    if cursor_moving:
        draw_centered_text(str(totalScore), CENTER_Y - 15, bigFont, get_color(totalScore))
        draw_centered_text("SCORE", CENTER_Y + 25, font, DIM_TEXT_COLOR)
    else:
        draw_centered_text(f"{lastPrize:+}", CENTER_Y - 15, bigFont, get_color(lastPrize))
        draw_centered_text("total " + str(totalScore), CENTER_Y + 25, font, DIM_TEXT_COLOR)
    
    if cursor_moving:
        draw_centered_text("press SPACE to stop the light", 540, font, TEXT_COLOR)
    else:
        draw_centered_text("press SPACE to play again", 540, font, TEXT_COLOR)
    
    draw_centered_text("Round " + str(roundNumber), 575, font, DIM_TEXT_COLOR)
    
    pygame.display.flip()

# MAIN GAME LOOP - runs continuously
while True:

    ### Main game logic ###
    frameCount = frameCount + 1
    if cursor_moving and frameCount % FRAMES_PER_STEP == 0: # If x % y == 0, then x is divisible by y
        pointer = (pointer + 1) % len(PRIZES)

    spacePressed = is_space_pressed()
    if spacePressed and cursor_moving:
        cursor_moving = False
        lastPrize = PRIZES[pointer]
        totalScore = totalScore + lastPrize
    elif spacePressed and not cursor_moving:
        cursor_moving = True
        roundNumber = roundNumber + 1


    ### Draw to the screen ###
    screen.fill(BACKGROUND)
    draw_ring(pointer)
    draw_centered_text("CYCLONE", 38, bigFont, TEXT_COLOR)
    
    if cursor_moving:
        draw_centered_text(str(totalScore), CENTER_Y - 15, bigFont, get_color(totalScore))
        draw_centered_text("SCORE", CENTER_Y + 25, font, DIM_TEXT_COLOR)
    else:
        draw_centered_text(f"{lastPrize:+}", CENTER_Y - 15, bigFont, get_color(lastPrize))
        draw_centered_text("total " + str(totalScore), CENTER_Y + 25, font, DIM_TEXT_COLOR)
    
    if cursor_moving:
        draw_centered_text("press SPACE to stop the light", 540, font, TEXT_COLOR)
    else:
        draw_centered_text("press SPACE to play again", 540, font, TEXT_COLOR)
    
    draw_centered_text("Round " + str(roundNumber), 575, font, DIM_TEXT_COLOR)

    ### Render everything and advance time at a steady framerate ###
    pygame.display.flip()
    clock.tick(60)

pygame.quit()