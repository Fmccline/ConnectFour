from GameBoard import GameBoard


class ConsecutivePieceCounter:

    @staticmethod
    def is_consecutive_piece(piece, color, counting_empty):
        if piece == color:
            return True
        elif counting_empty and piece == GameBoard.EMPTY_PIECE:
            return True
        else:
            return False

    @staticmethod
    def get_vertical_pieces(color, column, row, game_board, counting_empty=False):
        consecutive_pieces = 0
        if counting_empty:
            consecutive_pieces += game_board.get_num_rows() - row - 1
        for row_num in reversed(range(0, row)):
            piece = game_board.get_piece(column, row_num)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    @staticmethod
    def get_west_pieces(color, column, row, game_board, counting_empty=False):
        consecutive_pieces = 0
        for column_num in reversed(range(0, column)):
            piece = game_board.get_piece(column_num, row)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    @staticmethod
    def get_east_pieces(color, column, row, game_board, counting_empty=False):
        consecutive_pieces = 0
        for column_num in range(column+1, game_board.get_num_columns()):
            piece = game_board.get_piece(column_num, row)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    @staticmethod
    def get_nw_pieces(color, column_num, row_num, game_board, counting_empty=False):
        consecutive_pieces = 0
        column = column_num
        for row in range(row_num+1, game_board.get_num_rows()):
            column -= 1
            piece = game_board.get_piece(column, row)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    @staticmethod
    def get_sw_pieces(color, column_num, row_num, game_board, counting_empty=False):
        consecutive_pieces = 0
        column = column_num
        for row in reversed(range(0, row_num)):
            column -= 1
            if column < 0:
                break
            piece = game_board.get_piece(column, row)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    @staticmethod
    def get_ne_pieces(color, column_num, row_num, game_board, counting_empty=False):
        consecutive_pieces = 0
        column = column_num
        for row in range(row_num+1, game_board.get_num_rows()):
            column += 1
            if column >= game_board.get_num_columns():
                break
            piece = game_board.get_piece(column, row)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces

    @staticmethod
    def get_se_pieces(color, column_num, row_num, game_board, counting_empty=False):
        consecutive_pieces = 0
        column = column_num
        for row in reversed(range(0, row_num)):
            column += 1
            if column >= game_board.get_num_columns():
                break
            piece = game_board.get_piece(column, row)
            if ConsecutivePieceCounter.is_consecutive_piece(piece, color, counting_empty):
                consecutive_pieces += 1
            else:
                break
        return consecutive_pieces
