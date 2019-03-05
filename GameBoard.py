
class GameBoard:
    EMPTY_PIECE = 0
    RED_PIECE = 1
    BLACK_PIECE = 2

    def __init__(self, num_columns, num_rows):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.pieces = None
        self.total_pieces = 0
        self.reset_board()

    def reset_board(self):
        self.total_pieces = 0
        self.pieces = [[self.EMPTY_PIECE for _ in range(self.num_rows)] for _ in range(self.num_columns)]

    def get_num_columns(self):
        return self.num_columns

    def get_num_rows(self):
        return self.num_rows

    def get_board_size(self):
        return self.get_num_columns(), self.get_num_rows()

    def can_make_move(self, column):
        if column is None:
            return False
        if column < 0 or column >= self.num_columns:
            return False
        top_row = self.num_rows - 1
        return self.pieces[column][top_row] == self.EMPTY_PIECE

    def get_all_possible_moves(self):
        moves = []
        for column in range(self.num_columns):
            if self.can_make_move(column):
                moves.append(column)
        return moves

    def make_move(self, column, player_color):
        row = self.get_first_empty_row(column)
        if row is None:
            raise Exception(f"Row is none given column {column}")
        self.pieces[column][row] = player_color
        self.total_pieces += 1

    def get_first_empty_row(self, column):
        if column is None:
            raise Exception("Column cannot be None!")
        pieces = self.pieces
        for row in range(self.num_rows):
            if pieces[column][row] == GameBoard.EMPTY_PIECE:
                return row
        return None

    def get_row(self, column):
        row = self.get_first_empty_row(column)
        row = self.num_rows - 1 if row is None else row - 1
        return row

    def get_piece(self, column, row):
        return self.pieces[column][row]

    def print_board(self):
        pieces = self.pieces
        for y in range(self.num_rows - 1, -1, -1):
            for x in range(self.num_columns):
                print(str(pieces[x][y]) + ' ', end='')
            print()

    def is_full_board(self):
        board_size = self.num_columns * self.num_rows
        return self.total_pieces >= board_size

    def get_pieces(self):
        return self.pieces
