from Player import Player


class HumanPlayer(Player):

    def __init__(self, color, game_board_view):
        super().__init__(color, game_board_view.game_board)
        self.game_board_view = game_board_view

    def take_turn(self):
        column = self.game_board_view.get_clicked_column()
        if column is not None:
            row = self.game_board.get_first_empty_row(column)
            if row is not None:
                print("Moving to column " + str(column))
                self.game_board.make_move(column, row, self.color)
                return True
        else:
            return False

    def get_played_pieces(self):
        if self.color == self.RED_PLAYER:
            played_pieces = self.game_board.get_red_pieces()
        elif self.color == self.BLACK_PLAYER:
            played_pieces = self.game_board.get_black_pieces()
        else:
            raise Exception("Player isn't Red or Black ing get_played_pieces")
        return played_pieces
