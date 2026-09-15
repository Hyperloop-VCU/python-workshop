""" 1.6: 

"""
from turtle import *

# setup
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
turtle = Turtle()
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("lightblue")  # Accepts names, hex codes, or RGB tuples
turtle.shape("turtle")

# main logic
def main_logic():
    ### do not modify above this line ###
    userInput = input("Enter command: ")

    if userInput == "left":
        turtle.left(45)
    elif userInput == "right":
        turtle.right(45)
    elif userInput == "forward":
        turtle.forward(100)
    elif userInput == "back":
        turtle.back(100)
    elif userInput == "exit":
        exit()
    else:
        turtle.forward(100)

    turtleX, turtleY = turtle.pos()
    print("Turtle position:", turtleX, turtleY)

### do not modify below this line ###
while True:
    main_logic()


