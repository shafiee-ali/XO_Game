from Entities.board import Board


class XOBoard(Board):
    def __init__(self, n, chain_size):
        super(XOBoard, self).__init__(n)
        self.chain_size = chain_size

    def vertical_match(self, x, y):
        i, j = x - self.chain_size - 1, y
        value = self.matrix[x][y]
        length = 0
        for _ in range(2 * self.chain_size):
            if self.matrix[i][j] == value:
                length += 1
            else:
                length = 0
            if length == self.chain_size:
                return True
            i += 1

    def horizonal_match(self, x, y):
        i, j = x, y - self.chain_size - 1
        value = self.matrix[x][y]
        length = 0
        for _ in range(2 * self.chain_size):
            if self.matrix[i][j] == value:
                length += 1
            else:
                length = 0
            if length == self.chain_size:
                return True
            j += 1

    def diagonal_match(self, x, y):
        i, j = x - self.chain_size-1, y - self.chain_size-1
        value = self.matrix[x][y]
        length = 0
        for _ in range(self.chain_size):
            if self.matrix[i][j] == value:
                length += 1
            else:
                length = 0
            if length == self.chain_size:
                return True
            i += 1
            j += 1

    def is_matched(self, x, y):
        return self.horizonal_match(x, y) or self.vertical_match(x, y) or self.diagonal_match(x, y)





