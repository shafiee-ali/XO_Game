from Entities.board import Board


class XOBoard(Board):
    def __init__(self, n):
        super(XOBoard, self).__init__(n)
        self.chain_size = 3


    # def is_matched(self):
        # for i in range(self.size):
        #     for j in range(self.size):



