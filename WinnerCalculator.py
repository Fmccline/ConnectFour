from GameBoard import GameBoard


class WinnerCalculator:

    def __init__(self, game_board):
        self.game_board = game_board
        self.pieces = game_board.get_pieces()
        self.total_columns, self.total_rows = game_board.get_board_size()

    def is_winner(self, color, game_board):
        self.game_board = game_board
        self.pieces = game_board.get_pieces()
        if self.is_vertical_win(color):
            return True
        elif self.is_horizontal_win(color):
            return True
        elif self.is_diagonal_win(color):
            return True
        else:
            return False

    def is_vertical_win(self, color):
        played_pieces = self.game_board.get_played_pieces(color)
        for column in self.pieces:
            consecutive_pieces = 0
            for piece in column:
                if piece == color:
                    played_pieces -= 1
                    consecutive_pieces += 1
                    if consecutive_pieces >= 4:
                        return True
                    if played_pieces + consecutive_pieces < 4:
                        return False
                else:
                    consecutive_pieces = 0
                if piece == GameBoard.EMPTY_PIECE:
                    break
        return False

    def is_horizontal_win(self, color):
        # Run through the 4th because it must contain one of the winning pieces
        column = 3
        for row in range(self.total_rows):
            if self.pieces[column][row] == color:
                west = self.get_west_pieces(color, column, row)
                east = self.get_east_pieces(color, column, row)
                total = west + 1 + east
                if total >= 4:
                    return True
        return False

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

    def is_diagonal_win(self, color):
        # The 4th row must contain one of the winning pieces in a diagonal win
        row = 3
        for column in range(0, self.total_columns):
            if self.pieces[column][row] == color:
                if self.is_diagonal_winner(color, column, row):
                    return True
        return False

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
