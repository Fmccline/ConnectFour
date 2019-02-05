from GameBoard import GameBoard


class Game:

    def __init__(self, game_board: GameBoard, red_player, black_player):
        self.game_board = game_board
        self.game_board.reset_board()
        self.total_columns, self.total_rows = game_board.get_board_size()
        self.red_player = red_player
        self.black_player = black_player
        self.current_player = red_player

    def take_turn(self):
        turn_taken = self.current_player.take_turn()
        if turn_taken is True:
            self.current_player = self.black_player if self.current_player == self.red_player else self.red_player

