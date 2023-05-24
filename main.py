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
snake_blocks = []
# Starting point
startx = 0

# Create 'snake'
for _ in range(3):
    s = Turtle("square")
    s.color("lime green")
    s.penup()
    s.goto(startx, 0)
    startx -= 20
    snake_blocks.append(s)

# Bool to check game state
game_on = True
# Start game
while game_on:
    # Move forward
    for snake in snake_blocks:
        snake.forward(20)
        screen.update()
        time.sleep(0.1)
        

# Exit on click
screen.exitonclick()