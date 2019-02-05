import random

from Player import Player


class RandomPlayer(Player):

    def __init__(self, color, game_board):
        super().__init__(color, game_board)
        self.num_columns = game_board.num_columns

    def take_turn(self):
        column = random.randint(0, self.num_columns)
        return self.game_board.make_move(column, self.color)
