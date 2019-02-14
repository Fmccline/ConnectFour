from GameBoard import GameBoard
from Player import Player
from PlayerFactory import PlayerFactory
from WinnerCalculator import WinnerCalculator


class Game:

    def __init__(self, game_board: GameBoard, red_player, black_player):
        self.game_board = game_board
        self.game_board.reset_board()
        self.total_columns, self.total_rows = game_board.get_board_size()
        self.red_player = red_player
        self.black_player = black_player
        self.current_player = self.red_player
        self.winner_calculator = WinnerCalculator(game_board)

    def take_turn(self):
        current_player = self.current_player
        turn_taken = current_player.take_turn()
        if turn_taken is True:
            if self.is_winner(current_player):
                return self.current_player
            else:
                self.current_player = self.black_player if current_player == self.red_player else self.red_player
                return None

    def is_winner(self, player):
        color = player.color
        return self.winner_calculator.is_winner(color, self.game_board)

