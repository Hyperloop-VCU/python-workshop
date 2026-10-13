from turtle import *

t = Turtle()

def triangle():
    size = 50
    angle = 120
    t.forward(size)
    t.left(angle)
    t.forward(size)
    t.left(angle)
    t.forward(size)
    t.left(angle)
    t.forward(size)
"""
Another way to do it, however you end up at a different place
size = 50
    angle = 60
    t.left(angle)
    t.forward(size)
    t.right(2*angle)
    t.forward(size)
    t.right(2*angle)
    t.forward(size)
"""



def main():
    triangle()
    mainloop()


main()