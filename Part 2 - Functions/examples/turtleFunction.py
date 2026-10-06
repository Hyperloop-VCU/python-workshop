

from turtle import *

t = Turtle() #this just creates a turtle object that you can apply functions to, will be discussed more later
def drawBox(t, shape, boxSize):
    t.shape(shape)
    t.forward(boxSize) #all sides are same size to make a square
    t.right(90) #a box has a 90 degree turn at each corner
    t.forward(boxSize)
    t.right(90)
    t.forward(boxSize)
    t.right(90)
    t.forward(boxSize)
    
drawBox(t, "turtle", 50)
mainloop()




