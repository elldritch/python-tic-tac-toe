"""
Defines a player for human interaction.
"""

from Player import Player

class HumanPlayer(Player):
    """
    A Player that takes orders from human input.
    """

    def think(self, game):
        """
        Takes human input.
        """
        print('\nYou are player ' + ('X' if game.get_player() == 0 else 'O') + ':')
        print('\nCurrent game state:')
        print(game, '\n')

        valid = False
        while not valid:
            move = input('Enter a move by selecting a position to take: ')

            try:
                move = int(move)
            except ValueError:
                print('Please enter an integer position.\n')

            valid, reason = game.is_valid_move(move)
            if not valid:
                print('Sorry, that move isn\'t valid;', reason.lower(), '\n')

        return move
