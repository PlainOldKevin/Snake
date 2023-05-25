# Imports
from turtle import Screen
from snake import Snake
from food import Food
import time

# Create screen and give characteristics
screen = Screen()
screen.setup(700, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize Snake and Food
snake = Snake()
food = Food()

# Listen for snake movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Bool to check game state
game_on = True

# Start game
while game_on:
    # Move forward
    screen.update()
    time.sleep(0.04)
    
    # Detect collision with food
    

    snake.move()

# Exit on click
screen.exitonclick()