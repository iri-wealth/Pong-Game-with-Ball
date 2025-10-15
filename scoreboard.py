"""The Scoreboard class with all its methods."""
import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.computer_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Player: {self.player_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 200)
        self.write(f"Computer: {self.computer_score}", align="center", font=("Courier", 24, "normal"))

    def player_point(self):
        self.player_score += 1
        self.update_scoreboard()

    def computer_point(self):
        self.computer_score += 1
        self.update_scoreboard()
