# Imports
from turtle import Turtle
import random as r

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
        random_x = r.randint(-330, 330)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)

    # Function to move somewhere else on screen
    def move(self):
        random_x = r.randint(-330, 330)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)