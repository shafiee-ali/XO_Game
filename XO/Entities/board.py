class Board:
    def __init__(self, n: int):
        if not Board.is_valid_board_size(n):
            raise Exception("wrong board size")

        self.size = n
        self.matrix = [['_' for j in range(n)] for i in range(n)]

    def __str__(self):
        res = ''
        for i in range(self.size):
            for j in range(self.size):
                res += str(self.matrix[i][j]) + ' '
            res += '\n'
        return res
    def fill_cell(self, x: int, y: int, value: int) -> None:
        """
        Take coordinates of a cell in board and fill it
        """
        if self.is_valid_cell(x, y):
            if self.is_empty_cell(x, y):
                self.matrix[x][y] = value
            else:
                raise Exception("This cell is already full")
        else:
            raise Exception("wrong coordinate")

    def is_valid_cell(self, x: int, y: int) -> None:
        if (0 <= x <= self.size - 1) and (0 <= y <= self.size - 1):
            return True
        return False

    def is_empty_cell(self, x, y):
        if self.is_valid_cell(x, y):
            return self.matrix[x][y] == '_'

    @staticmethod
    def is_valid_board_size(n: int):
        return n != 0
