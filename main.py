# Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create screen and give characteristics
screen = Screen()
screen.setup(700, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize Snake, Food, Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    time.sleep(0.05)
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase_score()

    snake.move()

# Exit on click
screen.exitonclick()