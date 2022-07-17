class Board:
    def __init__(self, n: int):
        self._size = n
        self.matrix = [[None for j in range(n)] for i in range(n)]

    def fill_cell(self, x: int, y: int, value: int) -> None:
        """
        Take coordinates of a cell in board and fill it
        """
        if self.is_valid_cell(x, y):
            self.matrix[x][y] = value
        else:
            raise Exception("wrong coordinate")

    def is_valid_cell(self, x: int, y: int) -> None:
        if (0 <= x <= self._size-1) and (0 <= y <= self._size-1):
            return True
        return False

