# Imports
from turtle import Screen
from snake import Snake
import time

# Create screen and give characteristics
screen = Screen()
screen.setup(700, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize Snake
snake = Snake()

# Bool to check game state
game_on = True

# Start game
while game_on:
    # Move forward
    screen.update()
    time.sleep(0.1)

    snake.move()

# Exit on click
screen.exitonclick()