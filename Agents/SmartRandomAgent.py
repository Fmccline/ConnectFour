import random

from Agents.Agent import Agent
from WinnerCalculator import WinnerCalculator


class SmartRandomAgent(Agent):
    def __init__(self, color):
        super().__init__(color)
        self.winner_calculator = WinnerCalculator()

    def get_move(self, game_board):
        num_columns = game_board.get_num_columns()
        column = -1
        self_win = self.get_winning_move(game_board)
        opponent_win = self.get_opponent_winning_move(game_board)
        if self_win is not None:
            column = self_win
        elif opponent_win is not None:
            column = opponent_win
        else:
            while game_board.can_make_move(column) is False:
                column = random.randint(0, num_columns)
        color_name = "RED" if self.color == Agent.RED_PLAYER else "BLACK"
        print(f"{color_name}'s best move: {column}")
        return column

    def get_winning_move(self, game_board):
        moves = game_board.get_all_possible_moves()
        for move in moves:
            new_board = game_board.make_copy()
            new_board.make_move(move, self.color)
            if self.winner_calculator.is_winner(self.color, new_board, move):
                return move
        return None

    def get_opponent_winning_move(self, game_board):
        color = Agent.RED_PLAYER if self.color == Agent.BLACK_PLAYER else Agent.BLACK_PLAYER
        moves = game_board.get_all_possible_moves()
        for move in moves:
            new_board = game_board.make_copy()
            new_board.make_move(move, color)
            if self.winner_calculator.is_winner(color, new_board, move):
                return move
        return None
