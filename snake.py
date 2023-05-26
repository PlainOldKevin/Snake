# Imports
from turtle import Turtle

# Constants
MOVE_DISTANCE = 20
START_POSITIONS = [(0, 0), (0, -20), (0, -40)]

class Snake:

    # Init method
    def __init__(self) -> None:
        # Define attributes
        self.snake_segments = []
        self.create()
        self.head = self.snake_segments[0]

    # Function to create snake
    def create(self):
        # Build snake
        for position in START_POSITIONS:
            self.add_segment(position)

    # Function to add a segment to the snake
    def add_segment(self, position):
        # Define snake segment attributes
        s = Turtle("square")
        s.color("lime green")
        s.penup()
        s.goto(position)
        self.snake_segments.append(s)

    # Function to extend snake on food collision
    def grow(self):
        self.add_segment(self.snake_segments[-1].position())

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

    # Function to move snake upwards
    def up(self):
        # Check if snake is going in opposite direction (no turning directly around)
        if self.head.heading() != 270:
            # Go up
            self.head.setheading(90)

    # Function to move snake downwards
    def down(self):
        # Check if snake is going in opposite direction (no turning directly around)
        if self.head.heading() != 90:
            # Go down
            self.head.setheading(270)

    # Function to move snake left
    def left(self):
        # Check if snake is going in opposite direction (no turning directly around)
        if self.head.heading() != 0:
            # Go left
            self.head.setheading(180)
    
    # Function to move snake right
    def right(self):
        # Check if snake is going in opposite direction (no turning directly around)
        if self.head.heading() != 180:
            # Go right
            self.head.setheading(0)

        