# Imports
from turtle import Turtle

# Constants
SCOREBOARD_TEXT = ('Courier', 18, 'bold')

class Scoreboard(Turtle):

    # Init method
    def __init__(self) -> None:
        # Define attributes
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        
        # Open data file and define highscore
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=SCOREBOARD_TEXT)
        self.hideturtle()

    # Function to increase score
    def increase_score(self):
        self.score += 1
        self.update_score()

    # Function to check & change high score
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()

    # Function to print 'Game Over' message
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=SCOREBOARD_TEXT)