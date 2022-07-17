class Player:
    def __init__(self, id: int):
        self.id = id

    @staticmethod
    def is_valid_player_numbers(m: int):
        return m != 0
