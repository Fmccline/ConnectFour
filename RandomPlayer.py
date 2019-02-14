import random

from Player import Player


class RandomPlayer(Player):

    def __init__(self, color, game_board):
        super().__init__(color, game_board)
        self.num_columns = self.game_board.num_columns

    def take_turn(self):
        column = -1
        while self.game_board.can_make_move(column) is False:
            column = random.randint(0, self.num_columns)
        self.game_board.make_move(column, self.color)
        return True
