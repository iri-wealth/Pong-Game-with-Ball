"""The game class performs all the logic for the Pong game."""
import turtle
import random
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, AI_SPEED, MAX_SCORE

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.screen.tracer(2)

        self.paddle_player = Paddle(-350, 0)
        self.paddle_computer = Paddle(350, 0)
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkeypress(self.paddle_player.move_up, "w")
        self.screen.onkeypress(self.paddle_player.move_down, "s")
        self.screen.onkeypress(self.ball.move_up, "Up")
        self.screen.onkeypress(self.ball.move_down, "Down")
        self.screen.onkeypress(self.ball.move_left, "Left")
        self.screen.onkeypress(self.ball.move_right, "Right")
        self.screen.onkeyrelease(self.ball.stop, "Up")
        self.screen.onkeyrelease(self.ball.stop, "Down")
        self.screen.onkeyrelease(self.ball.stop, "Left")
        self.screen.onkeyrelease(self.ball.stop, "Right")

    def move_computer_paddle(self):
        move = random.choice([-1, 0, 1])
        new_y = self.paddle_computer.ycor() + move * AI_SPEED
        if -SCREEN_HEIGHT / 2 + 50 < new_y < SCREEN_HEIGHT / 2 - 50:
            self.paddle_computer.goto(self.paddle_computer.xcor(), new_y)

    def play_round(self):
        game_is_on = True
        while game_is_on:
            self.screen.update()
            self.ball.move()
            self.move_computer_paddle()

            # Detect collision with top and bottom walls
            if self.ball.ycor() > 290 or self.ball.ycor() < -290:
                self.ball.bounce_y()

            # Detect collision with paddles
            if (self.ball.distance(self.paddle_computer) < 50 and self.ball.xcor() > 320) or \
               (self.ball.distance(self.paddle_player) < 50 and self.ball.xcor() < -320):
                self.ball.bounce_x()

            # Detect when computer paddle misses
            if self.ball.xcor() > 380:
                self.ball.reset_position()
                self.scoreboard.player_point()
                if self.scoreboard.player_score >= MAX_SCORE:
                    return "Player"

            # Detect when player paddle misses
            if self.ball.xcor() < -380:
                self.ball.reset_position()
                self.scoreboard.computer_point()
                if self.scoreboard.computer_score >= MAX_SCORE:
                    return "Computer"

        return None

    def play(self):
        while True:
            winner = self.play_round()
            if winner:
                self.screen.clear()
                self.screen.bgcolor("darkblue")
                message = turtle.Turtle()
                message.color("white")
                message.penup()
                message.hideturtle()
                message.write(f"The game is over! The winner is: {winner}", align="center", font=("Courier", 24, "normal"))
                time.sleep(3)
                message.clear()

                play_again = self.screen.textinput("Play Again", "Do you want to play again? (y/n): ")
                if play_again.lower() != 'y':
                    message.write("Thank you for playing, goodbye!", align="center", font=("Courier", 24, "normal"))
                    time.sleep(2)
                    break
                else:
                    self.__init__()  # Reset the game

        self.screen.bye()
