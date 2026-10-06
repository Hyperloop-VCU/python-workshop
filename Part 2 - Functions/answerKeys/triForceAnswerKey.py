from turtle import *


t = Turtle()


def Triangle(turtle, size):
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    

#where do you end up from here, and where should you be? 






def Triforce(turtle, size):
    Triangle(turtle, size)  
    Triangle(turtle, size)
    turtle.left(120)
    turtle.forward(size)
    Triangle(turtle,size)
    



Triforce(t, 100)
mainloop()