# Imports
from turtle import Turtle, Screen
import time

# Create screen and give characteristics
screen = Screen()
screen.setup(700, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# List to hold snake parts (turtles)
snake_segments = []
# Starting point
startx = 0

# Create 'snake'
for _ in range(3):
    s = Turtle("square")
    s.color("lime green")
    s.penup()
    s.goto(startx, 0)
    startx -= 20
    snake_segments.append(s)

# Bool to check game state
game_on = True

# Start game
while game_on:
    # Move forward
    screen.update()
    time.sleep(0.3)

    # For loop to make segments stay together, range params are 'start, stop, step'
    for snake_seg in range(len(snake_segments) - 1, 0, -1):
        # Find second to last snake segment's coordinates
        newx = snake_segments[snake_seg - 1].xcor()
        newy = snake_segments[snake_seg - 1].ycor()
        # And move the last snake segment to its spot before moving second-to-last segment forward
        # Keeps the snake together on screen
        snake_segments[snake_seg].goto(newx, newy)
        #Update screen
        screen.update()
    snake_segments[0].forward(20)

# Exit on click
screen.exitonclick()