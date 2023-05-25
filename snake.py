# Imports
from turtle import Turtle

# Constants
MOVE_DISTANCE = 20

class Snake:

    # Init method
    def __init__(self) -> None:
        self.snake_segments = []
        self.create()

    # Function to create snake
    def create(self):
        # Starting point
        startx = 0
        # Build snake
        for _ in range(3):
            s = Turtle("square")
            s.color("lime green")
            s.penup()
            s.goto(startx, 0)
            startx -= 20
            self.snake_segments.append(s)

    # Function to move snake
    def move(self):
        # For loop to make segments stay together, range params are 'start, stop, step'
        for snake_seg in range(len(self.snake_segments) - 1, 0, -1):
            # Find second to last snake segment's coordinates
            newx = self.snake_segments[snake_seg - 1].xcor()
            newy = self.snake_segments[snake_seg - 1].ycor()
            # And move the last snake segment to its spot before moving second-to-last segment forward
            # Keeps the snake together on screen
            self.snake_segments[snake_seg].goto(newx, newy)
        # Move snake forward
        self.snake_segments[0].forward(20)