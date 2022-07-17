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
        self.next()


    def next(self):
        """

        :return:
        """
        self.curr_player_id = (self.curr_player_id + 1) % self.players_count

    def get_current_player(self):
        return self.curr_player_id

    def is_end_game(self):
        return 0

    def print_board(self):
        print(self.board)

    def is_matched(self):
        pass