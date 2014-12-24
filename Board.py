"""
Defines a game board.
"""

class IllegalMoveException(Exception):
    """
    An exception representing an illegal move.
    """
    pass

class Board(object):
    """
    Is a tic-tac-toe board which enforces game rules.
    """
    EMPTY_SPOT = ' '
    X_SPOT = 'X'
    O_SPOT = 'O'

    PLAYER_X_WINS = 'Player X has won!'
    PLAYER_O_WINS = 'Player O has won!'
    UNWINNABLE = 'This game is unwinnable.'
    INCOMPLETE = 'This game is incomplete.'

    def __init__(self):
        self.board = [[Board.EMPTY_SPOT for _ in range(3)] for _ in range(3)]
        self.turn = 0

    def is_valid_move(self, position):
        """
        Returns a tuple of (validity, reason for failure). If the move is valid, reason for failure is empty.
        """
        position -= 1
        reason = ''

        if position < 0 or position > 8:
            reason = 'Cell not on board.'
        elif self.board[position // len(self.board)][position % len(self.board)] is not Board.EMPTY_SPOT:
            reason = 'Cell already taken.'
        elif self.get_completion_state() is not Board.INCOMPLETE:
            reason = 'Game already completed.'

        return (len(reason) is 0, reason)

    def make_move(self, position):
        """
        Make the next move in the game. Throws an IllegalMoveException if that move is illegal.
        """
        valid, reason = self.is_valid_move(position)
        if not valid:
            raise IllegalMoveException(reason)

        position -= 1

        self.board[position // len(self.board)][position % len(self.board)] = Board.X_SPOT if self.get_player() == 0 else Board.O_SPOT
        self.turn += 1

    def get_player(self):
        """
        Return the current player.
        """
        return self.turn % 2

    def is_complete(self):
        """
        Returns true if the game is complete and false otherwise.
        """
        return self.get_completion_state() is not Board.INCOMPLETE

    def get_completion_state(self):
        """
        Returns either PLAYER_X_WINS, PLAYER_O_WINS, UNWINNABLE, or INCOMPLETE.
        """
        if self.check_win(Board.X_SPOT):
            return Board.PLAYER_X_WINS
        elif self.check_win(Board.O_SPOT):
            return Board.PLAYER_O_WINS
        elif sum([sum([1 if cell is Board.EMPTY_SPOT else 0 for cell in row]) for row in self.board]) == 0:
            return Board.UNWINNABLE
        else:
            return Board.INCOMPLETE

    def check_win(self, token):
        """
        Checks whether a player has won.
        """
        win_by_row = self.exists_uniform_row(self.board, token)

        transpose = zip(*self.board)
        win_by_col = self.exists_uniform_row(transpose, token)

        diagonals = [
            [self.board[i][i] for i in range(len(self.board))],
            [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))],
        ]

        win_by_diag = self.exists_uniform_row(diagonals, token)

        return win_by_row or win_by_col or win_by_diag

    @staticmethod
    def exists_uniform_row(matrix, token):
        """
        Check if an array of arrays has at least one array that is composed entirely of token.
        """
        for row in matrix:
            won = True

            for element in row:
                if element != token:
                    won = False

            if won:
                return won

        return False

    def __str__(self):
        return '\n-----------------\n'.join([
            ' ' + ' | '.join(
                ' ' + row[i] + ' ' if not row[i] == Board.EMPTY_SPOT else '(' + str(row_number * 3 + i + 1)+ ')' for i in range(len(row))
            )
            for row_number, row in enumerate(self.board)
        ]) + '\n' + self.get_completion_state()
