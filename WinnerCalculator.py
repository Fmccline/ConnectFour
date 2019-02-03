from GameBoard import GameBoard


class WinnerCalculator:

    def __init__(self, game_board):
        self.game_board = game_board
        self.pieces = game_board.get_pieces()
        self.total_columns, self.total_rows = game_board.get_board_size()

    def is_winner(self, player, game_board):
        self.game_board = game_board
        self.pieces = game_board.get_pieces()
        if self.is_vertical_win(player):
            print("Vertical")
            return True
        elif self.is_horizontal_win(player):
            print("Horizontal")
            return True
        elif self.is_diagonal_win(player):
            print("Diagonal")
            return True
        else:
            return False

    def is_vertical_win(self, player):
        played_pieces = player.get_played_pieces()
        for column in self.pieces:
            consecutive_pieces = 0
            for piece in column:
                if piece == player.color:
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

    def is_horizontal_win(self, player):
        played_pieces = player.get_played_pieces()
        for row_num in range(self.total_rows):
            consecutive_pieces = 0
            for col_num in range(self.total_columns):
                piece = self.pieces[col_num][row_num]
                if piece == player.color:
                    played_pieces -= 1
                    consecutive_pieces += 1
                    if consecutive_pieces >= 4:
                        return True
                    if played_pieces + consecutive_pieces < 4:
                        return False
                else:
                    consecutive_pieces = 0
        return False

    def is_diagonal_win(self, player):
        # Rows 3 and 4 must contain one of the winning pieces in a diagonal win
        # I chose to use row 3 arbitrarily
        row = 3
        for column in range(0, self.total_columns):
            if self.pieces[column][row] == player.color:
                if self.is_diagonal_winner(player, column, row):
                    return True
        return False

    def is_diagonal_winner(self, player, column, row):
        nw = self.get_nw_pieces(player, column, row)
        ne = self.get_ne_pieces(player, column, row)
        sw = self.get_sw_pieces(player, column, row)
        se = self.get_se_pieces(player, column, row)

        nw_se = nw + 1 + se
        ne_sw = ne + 1 + sw
        return nw_se >= 4 or ne_sw >= 4

    def get_nw_pieces(self, player, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in range(row_num+1, self.total_rows):
            column -= 1
            if column >= 0 and self.pieces[column][row] == player.color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces


    def get_sw_pieces(self, player, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in reversed(range(0, row_num)):
            column -= 1
            if column >= 0 and self.pieces[column][row] == player.color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def get_ne_pieces(self, player, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in range(row_num+1, self.total_rows):
            column += 1
            if column < self.total_columns and self.pieces[column][row] == player.color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    def get_se_pieces(self, player, column_num, row_num):
        consecutive_pieces = 0
        column = column_num
        for row in reversed(range(0, row_num)):
            column += 1
            if column < self.total_columns and self.pieces[column][row] == player.color:
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces
