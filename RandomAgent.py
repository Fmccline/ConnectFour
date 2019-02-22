import random

from Agent import Agent


class RandomAgent(Agent):

    def __init__(self, color, game_board):
        super().__init__(color, game_board)
        self.num_columns = game_board.get_num_columns()

    def get_move(self, game_board):
        column = -1
        while game_board.can_make_move(column) is False:
            column = random.randint(0, self.num_columns)
        return column

