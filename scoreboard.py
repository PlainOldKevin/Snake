# Imports
from turtle import Turtle

# Constants
SCOREBOARD_TEXT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    # Init method
    def __init__(self) -> None:
        # Define attributes
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=SCOREBOARD_TEXT)
        self.hideturtle()

    # Function to increase score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=SCOREBOARD_TEXT)