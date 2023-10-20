from turtle import Turtle, Screen
from random import random
from classes import *

if __name__ == '__main__':
    # inits turtle screen object to draw on
    canvas = Screen()
    canvas.setworldcoordinates(0, canvas.window_height(), canvas.window_width(), 0)
    canvas.tracer(0)
    
    # creates turtle drawing object and attaches to current screen object
    pen = Turtle()
    # setting defaults for turtle drawing object
    pen.hideturtle()
    pen.setheading(90)
    pen.pendown()
    pen.pencolor('black')

    sim = SIMULATION()
    sim.update_grid(canvas)

    canvas.mainloop()