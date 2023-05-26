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
        # Move food to new spot on screen
        food.move()
        # Grow snake 1 segment
        snake.grow()
        # Increase game score
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for seg in snake.snake_segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()

    # Move snake
    snake.move()

# Exit on click
screen.exitonclick()