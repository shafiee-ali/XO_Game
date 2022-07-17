from Entities.xo_board import XOBoard
from Entities.player import Player


class XOGame:
    def __init__(self, n: int, m: int):
        """
        :param n: Board size
        :param m: Number of players
        """

        if not Player.is_valid_player_numbers(m):
            raise Exception("wrong player numbers")

        self.players_count = m
        self.board = XOBoard(n, 3)
        self.players = [Player(i) for i in range(self.players_count)]
        self.curr_player_id = 0
        self._game_over = False
        self._winner = None

    def action(self, x: int, y: int):
        """

        :param x:
        :param y:
        :return:
        """
        self.board.fill_cell(x, y, self.curr_player_id)
        self.next()
        self._is_end_game(x, y)


    def next(self):
        """
        :return:
        """
        self.curr_player_id = (self.curr_player_id + 1) % self.players_count

    def get_current_player(self):
        return self.curr_player_id

    def game_over(self):
        return self._game_over

    def _is_end_game(self, x, y):
        if self.board.is_matched(x, y):
            self._game_over = True
            self._winner = self.board[x][y]

    def winner(self):
        return self._winner

    def print_board(self):
        print(self.board)

    def is_matched(self):
        pass