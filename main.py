""" The Pong Game:
Requirements:
1. The game should be implemented using object-oriented programming principles.
2. The game should include a player and a computer opponent.
3. The player should be able to control the paddles using the keyboard.
4. The computer opponent should have a simple AI algorithm to make decisions.
5. The game should have a scoring system where the player's score increases when they win a round.
6. The game should display the current score and the winner at the end of each round.
7. The game should have a difficulty level setting that affects the computer opponent's AI algorithm.
The game should be displayed in the Turtle screen so, that the game can be played in a graphical environment.
"""

from game import Game

if __name__ == "__main__":
    game = Game()
    game.play()