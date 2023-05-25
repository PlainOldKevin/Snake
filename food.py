# Imports
from turtle import Turtle
import random as r

# Constants
XCOORDS = r.randint(-330, 330)
YCOORDS = r.randint(-280, 280)

class Food(Turtle):
    
    # Init method
    def __init__(self) -> None:
        # Define attributes
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(XCOORDS, YCOORDS)