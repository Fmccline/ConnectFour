from GameBoard import GameBoard
from WinnerCalculator import WinnerCalculator


class Game:

    def __init__(self, game_board: GameBoard, red_player, black_player):
        self.game_board = game_board
        self.game_board.reset_board()
        self.total_columns, self.total_rows = game_board.get_board_size()
        self.red_player = red_player
        self.black_player = black_player
        self.current_player = self.red_player
        self.winner_calculator = WinnerCalculator()

    def take_turn(self):
        game_board = self.game_board
        current_player = self.current_player
        move = current_player.get_move(game_board)
        if game_board.can_make_move(move):
            game_board.make_move(move, current_player.color)
            if self.is_winner(current_player, move):
                return self.current_player
            else:
                self.current_player = self.black_player if current_player == self.red_player else self.red_player
                return None

    def is_winner(self, player, move):
        color = player.color
        # return self.winner_calculator.is_winner(color, self.game_board)
        return self.winner_calculator.is_winner(color, self.game_board, move)


