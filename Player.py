"""
Defines the player contract.
"""

class Player(object):
    """
    A generic Player object. Enforces the need to think.
    """

    def think(self, game):
        """
        Requires players to think.
        """
        raise NotImplementedError()
