"""The Ball class with its attributes and methods."""
import turtle
from constants import BALL_SPEED

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.dx = 0
        self.dy = 0

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy) # xcor and yor are x and y coordinates.

    def move_up(self):
        self.dy = BALL_SPEED

    def move_down(self):
        self.dy = -BALL_SPEED

    def move_left(self):
        self.dx = -BALL_SPEED

    def move_right(self):
        self.dx = BALL_SPEED

    def stop(self):
        self.dx = 0
        self.dy = 0

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.stop()
