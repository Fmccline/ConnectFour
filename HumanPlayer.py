from Player import Player


class HumanPlayer(Player):

    def __init__(self, color, game_board_view):
        super().__init__(color, game_board_view.game_board)
        self.game_board_view = game_board_view

    def take_turn(self):
        column = self.game_board_view.get_clicked_column()
        if column is not None and self.game_board.can_make_move(column):
            self.game_board.make_move(column, self.color)
            return True
        else:
            return False

