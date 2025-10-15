""" All the methods that the class Paddle will need to be implemented """
import turtle
from constants import SCREEN_HEIGHT, MOVE_SPEED

class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        new_y = self.ycor() + MOVE_SPEED
        if new_y < SCREEN_HEIGHT / 2 - 50:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_SPEED
        if new_y > -SCREEN_HEIGHT / 2 + 50:
            self.goto(self.xcor(), new_y)
