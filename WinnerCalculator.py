class WinnerCalculator:

    def __init__(self):
        self.game_board = None
        self.pieces = None
        self.total_columns, self.total_rows = 0, 0

    def is_winner(self, color, game_board, column):
        self.game_board = game_board
        self.pieces = game_board.get_pieces()
        self.total_columns, self.total_rows = game_board.get_board_size()
        row = self.get_row(column)
        is_vertical_win = self.is_vertical_winner(color, column, row)
        is_horizontal_win = self.is_horizontal_winner(color, column, row)
        is_diagonal_win = self.is_diagonal_winner(color, column, row)
        return is_vertical_win or is_horizontal_win or is_diagonal_win

    def get_row(self, column):
        row = self.game_board.get_first_empty_row(column)
        row = self.total_rows - 1 if row is None else row - 1
        return row

    def is_vertical_winner(self, color, move, row):
        pieces = self.pieces[move]
        consecutive = 0
        for piece_index in reversed(range(0, row)):
            piece = pieces[piece_index]
            if piece == color:
                consecutive += 1
            else:
                return False
            if consecutive == 3:
                return True
        return False

    def is_horizontal_winner(self, color, column, row):
        west = self.get_west_pieces(color, column, row)
        east = self.get_east_pieces(color, column, row)
        return west + 1 + east >= 4

    def get_west_pieces(self, color, column, row):
        consecutive_pieces = 0
        for column_num in reversed(range(0, column)):
            if self.pieces[column_num][row] == color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def get_east_pieces(self, color, column, row):
        consecutive_pieces = 0
        for column_num in range(column+1, self.total_columns):
            if self.pieces[column_num][row] == color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def is_diagonal_winner(self, color, column, row):
        nw = self.get_nw_pieces(color, column, row)
        ne = self.get_ne_pieces(color, column, row)
        sw = self.get_sw_pieces(color, column, row)
        se = self.get_se_pieces(color, column, row)

        nw_se = nw + 1 + se
        ne_sw = ne + 1 + sw
        return nw_se >= 4 or ne_sw >= 4

    def get_nw_pieces(self, color, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in range(row_num+1, self.total_rows):
            column -= 1
            if column >= 0 and self.pieces[column][row] == color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def get_sw_pieces(self, color, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in reversed(range(0, row_num)):
            column -= 1
            if column >= 0 and self.pieces[column][row] == color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def get_ne_pieces(self, color, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in range(row_num+1, self.total_rows):
            column += 1
            if column < self.total_columns and self.pieces[column][row] == color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def get_se_pieces(self, color, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in reversed(range(0, row_num)):
            column += 1
            if column < self.total_columns and self.pieces[column][row] == color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces
