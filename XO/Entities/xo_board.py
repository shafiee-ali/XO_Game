from Entities.xo_board import XOBoard
from Entities.player import Player


class XOGame:
    def __init__(self, n: int, m: int):
        """
        :param n: Board size
        :param m: Number of players
        """
        if n == 0:
            raise Exception("wrong board size")
        if m == 0:
            raise Exception("wrong player numbers")

        self.players_count = m
        self.board = XOBoard(n)
        self.players = [Player(i) for i in range(self.players_count)]
        self.curr_player_id = 0

    def action(self, x: int, y: int):
        """

        :param x:
        :param y:
        :return:
        """
        self.board.fill_cell(x, y, self.curr_player_id)
        self.next_player()


    def next_player(self):
        """

        :return:
        """
        self.curr_player_id = (self.curr_player_id + 1) % self.players

    def is_end_game(self):
        return self.board.

    def next(self, ):