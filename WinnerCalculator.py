from ConsecutivePieceCounter import ConsecutivePieceCounter


class WinnerCalculator:

    def __init__(self):
        self.game_board = None
        self.pieces = None
        self.total_columns, self.total_rows = 0, 0

    def is_winner(self, color, game_board, last_move):
        self.game_board = game_board
        self.pieces = game_board.get_pieces()
        self.total_columns, self.total_rows = game_board.get_board_size()
        row = game_board.get_row(last_move)
        is_vertical_win = self.is_vertical_winner(color, last_move, row)
        is_horizontal_win = self.is_horizontal_winner(color, last_move, row)
        is_diagonal_win = self.is_diagonal_winner(color, last_move, row)
        return is_vertical_win or is_horizontal_win or is_diagonal_win

    def is_vertical_winner(self, color, move, row):
        consecutive_pieces = ConsecutivePieceCounter.get_vertical_pieces(color, move, row, self.game_board)
        return consecutive_pieces >= 3

    def is_horizontal_winner(self, color, column, row):
        west = ConsecutivePieceCounter.get_west_pieces(color, column, row, self.game_board)
        east = ConsecutivePieceCounter.get_east_pieces(color, column, row, self.game_board)
        return west + 1 + east >= 4

    def is_diagonal_winner(self, color, column, row):
        nw = ConsecutivePieceCounter.get_nw_pieces(color, column, row, self.game_board)
        ne = ConsecutivePieceCounter.get_ne_pieces(color, column, row, self.game_board)
        sw = ConsecutivePieceCounter.get_sw_pieces(color, column, row, self.game_board)
        se = ConsecutivePieceCounter.get_se_pieces(color, column, row, self.game_board)

        nw_se = nw + 1 + se
        ne_sw = ne + 1 + sw
        return nw_se >= 4 or ne_sw >= 4
