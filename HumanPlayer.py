from Player import Player


class HumanPlayer(Player):

    def __init__(self, color, game_board_view):
        super().__init__(color)
        self.game_board_view = game_board_view

    def take_turn(self, game_board):
        column = self.game_board_view.get_clicked_column()
        if column is not None:
            row = game_board.get_first_empty_row(column)
            if row is not None:
                print("Moving to column " + str(column))
                game_board.make_move(column, row, self.color)
                return True
        else:
            return False


