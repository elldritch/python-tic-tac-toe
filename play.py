"""
Plays a game of tic-tac-toe.
"""

from Board import Board
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer, DumbPlayer


def run_game(players):
    game = Board()

    while not game.is_complete():
        player = game.get_player()
        move = players[player].think(game)

        print('\n' + 'Player ' + ('X' if player is 0 else 'O') + ' moving to take ' + str(move) + '.')
        game.make_move(move)
        print(str(game))

        if game.is_complete():
            print('')
        else:
            print('\n-----------------------------------------------')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Plays tic-tac-toe.')
    parser.add_argument('players',
                        metavar='game-type',
                        type=str,
                        choices=[
                            'DvD',
                            'SvD',
                            'PvD',
                            'SvS',
                            'PvS',
                            'PvP'
                        ],
                        help='The type of game to play; "D" indicates a dumb player, "S" a smart player, and "P" a human player.')
    args = parser.parse_args()

    players = args.players.split('v')
    player_map = {'D': DumbPlayer, 'S': ComputerPlayer, 'P': HumanPlayer}

    run_game([player_map[player]() for player in players])
