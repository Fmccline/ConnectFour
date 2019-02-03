
class GameBoard:
    EMPTY_PIECE = 0
    RED_PIECE = 1
    BLACK_PIECE = 2

    def __init__(self, num_columns, num_rows):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.pieces = []
        self.black_pieces = 0
        self.red_pieces = 0
        self.reset_board()

    def reset_board(self):
        self.pieces = []
        self.black_pieces = 0
        self.red_pieces = 0
        for column_num in range(self.num_columns):
            column = []
            for row_num in range(self.num_rows):
                column.append(self.EMPTY_PIECE)
            self.pieces.append(column)

    def get_pieces(self):
        return self.pieces

    def get_black_pieces(self):
        return self.black_pieces

    def get_red_pieces(self):
        return self.red_pieces

    def get_first_empty_row(self, column):
        pieces = self.pieces
        for row in range(len(pieces[column])):
            if pieces[column][row] == GameBoard.EMPTY_PIECE:
                return row
        return None

    def make_move(self, column, row, player_color):
        self.pieces[column][row] = player_color
        if player_color == self.RED_PIECE:
            self.red_pieces += 1
        elif player_color == self.BLACK_PIECE:
            self.black_pieces += 1
        else:
            raise Exception('Player color is neither black of red in make_move. Color is ' + str(player_color))

    def print_board(self):
        pieces = self.pieces
        for y in range(self.num_rows - 1, -1, -1):
            for x in range(self.num_columns):
                print(str(pieces[x][y]) + ' ', end='')
            print()

    def get_board_size(self):
        return self.num_columns, self.num_rows
