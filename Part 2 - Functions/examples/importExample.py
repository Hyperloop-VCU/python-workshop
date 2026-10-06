#multiple ways to import, that changes how you call imported functions
import turtle
#this imports the whole turtle module
#however to access the functions i need to refernce the module first
t = turtle.Turtle()
t.forward(500)

from turtle import *
#this imports the whole turtle module, however the functions are accesible without using the module name

p = Turtle()
p.forward(500)



