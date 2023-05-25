# Imports
from turtle import Turtle

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