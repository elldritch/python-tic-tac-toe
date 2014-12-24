"""
Defines computer players.
"""

from Player import Player
from random import randint

class DumbPlayer(Player):
    """
    A Player that selects moves at random.
    """

    def think(self, game):
        """
        WARNING: Doesn't actually think.
        """
        move = 0
        valid = False

        while not valid:
            move = randint(1, 9)
            valid, _ = game.is_valid_move(move)

        return move


class ComputerPlayer(Player):
    """
    A smarter computer player.
    """

    def think(self, game):
        """
        Left as an exercise for the reader.
        """
        raise NotImplementedError('The computer doesn\'t know how to be smart yet!')
