# Imports
from turtle import Turtle

class Scoreboard(Turtle):

    # Init method
    def __init__(self) -> None:
        # Define attributes
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))

    # Function to increase score
    def increase_score(self):
        self.score += 1