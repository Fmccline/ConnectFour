
class GameBoard:
    EMPTY_PIECE = 0
    RED_PIECE = 1
    BLACK_PIECE = 2

    def __init__(self, num_columns, num_rows):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.pieces = []
        self.played_pieces = 0
        self.reset_board()

    def reset_board(self):
        self.played_pieces = 0
        self.pieces = []
        for column_num in range(self.num_columns):
            column = []
            for row_num in range(self.num_rows):
                column.append(self.EMPTY_PIECE)
            self.pieces.append(column)

    def get_pieces(self):
        return self.pieces

    def get_first_empty_row(self, column):
        pieces = self.pieces
        for row in range(len(pieces[column])):
            if pieces[column][row] == GameBoard.EMPTY_PIECE:
                return row
        return None

    def make_move(self, column, row, player):
        self.pieces[column][row] = player
        self.played_pieces += 1

    def print_board(self):
        pieces = self.pieces
        for y in range(self.num_rows - 1, -1, -1):
            for x in range(self.num_columns):
                print(str(pieces[x][y]) + ' ', end='')
            print()

    def get_board_size(self):
        return self.num_columns, self.num_rows
