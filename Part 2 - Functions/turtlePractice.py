from turtle import *

t = Turtle() # this is something called a class, this will be explained at a later date. think of it like bringing the turtle to existence.
#basically stating that the variable t is actually an object we defined as a turtle

#Each of the below lines are seperate functions
t.shape("turtle") #defines the shape of the turtle, we are applying this function to t
t.forward(50)#what do you think the below functions do?
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)

#before running, what do you think these list of functions actually do?
#try thinking of an answer before scrolling down













x = 5
def numbers():
    x = 10
    y = 10


def main():
    # Your code goes here
    print("x=", x,"\n")
    print("y=", y)






if __name__ == "__main__":
    main()














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





#drawBox(t,"turtle", 50, 90)






















print("hello world")
#Now print it one million times


















t.setheading(45)
t.forward(50)



mainloop()