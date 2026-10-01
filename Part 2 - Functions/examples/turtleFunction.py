

from turtle import *

t = Turtle()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#if you guessed create a box, you were right.
#but what if you want to make a 100 boxes? 
#Its time to learn how to make your own function

def drawBox(turtle, shape ,boxWidth, boxHeight):
    t.shape(shape)
    t.forward(boxWidth)
    t.right(boxHeight)
    t.forward(boxWidth)
    t.right(boxHeight)
    t.forward(boxWidth)
    t.right(boxHeight)
    t.forward(boxWidth)
    t.right(boxHeight)

