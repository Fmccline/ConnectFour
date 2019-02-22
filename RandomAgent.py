import random

from Agent import Agent


class RandomAgent(Agent):

    def __init__(self, color):
        super().__init__(color)

    def get_move(self, game_board):
        num_columns = game_board.get_num_columns()
        column = -1
        while game_board.can_make_move(column) is False:
            column = random.randint(0, num_columns)
        return column

