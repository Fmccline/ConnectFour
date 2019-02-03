from GameBoard import GameBoard


class Game:

    def __init__(self, game_board: GameBoard, red_player, black_player):
        self.game_board = game_board
        self.total_columns, self.total_rows = game_board.get_board_size()
        self.red_player = red_player
        self.black_player = black_player
        self.current_player = red_player

    def take_turn(self):
        turn_taken = self.current_player.take_turn()
        if turn_taken is True:
            self.current_player = self.black_player if self.current_player == self.red_player else self.red_player
            print("Current turn: " + str(self.current_player))

    # def is_winner(self, player):
    #     pieces = self.game_board.get_pieces()
    #     if self.is_vertical_win(pieces, player):
    #         print("Vertical")
    #         return True
    #     elif self.is_horizontal_win(pieces, player):
    #         print("Horizontal")
    #         return True
    #     else:
    #         return False
    #
    # def is_vertical_win(self, pieces, player):
    #     played_pieces = player.get_played_pieces()
    #     for column in pieces:
    #         consecutive_pieces = 0
    #         for piece in column:
    #             if piece == player.color:
    #                 played_pieces -= 1
    #                 consecutive_pieces += 1
    #                 if consecutive_pieces >= 4:
    #                     return True
    #                 if played_pieces + consecutive_pieces < 4:
    #                     return False
    #             else:
    #                 consecutive_pieces = 0
    #             if piece == GameBoard.EMPTY_PIECE:
    #                 break
    #     return False
    #
    # def is_horizontal_win(self, pieces, player):
    #     played_pieces = player.get_played_pieces()
    #     for row_num in range(self.total_rows):
    #         consecutive_pieces = 0
    #         for col_num in range(self.total_columns):
    #             piece = pieces[col_num][row_num]
    #             if piece == player.color:
    #                 played_pieces -= 1
    #                 consecutive_pieces += 1
    #                 if consecutive_pieces >= 4:
    #                     return True
    #                 if played_pieces + consecutive_pieces < 4:
    #                     return False
    #             else:
    #                 consecutive_pieces = 0
    #     return False
    #
    # # TODO: finish diagonal win
    # def is_diagonal_win(self, pieces, player):
    #     # Rows 3 and 4 must contain one of the winning pieces in a diagonal win
    #     # I chose to use row 3 arbitrarily
    #     row = 3
    #     for column in range(0, self.total_columns):
    #         if is_diagonal_winner(column, row, player):
    #             return True
    #     return False
    #
    # def get_nw_pieces(self, pieces, player, column_num, row_num):
    #     consecutive_pieces = 0
    #     column = column_num
    #     for row in range(row_num+1, self.total_rows):
    #         column -= 1
    #         if column >= 0 and pieces[column][row] == player.color:
    #             consecutive_pieces += 1
    #         else:
    #             return consecutive_pieces
    #
    # def get_sw_pieces(self, pieces, player, column_num, row_num):
    #     consecutive_pieces = 0
    #     column = column_num
    #     for row in reversed(range(0, row_num)):
    #         column -= 1
    #         if column >= 0 and pieces[column][row] == player.color:
    #             consecutive_pieces += 1
    #         else:
    #             return consecutive_pieces
    #
    # def get_ne_pieces(self, pieces, player, column_num, row_num):
    #     consecutive_pieces = 0
    #     column = column_num
    #     for row in range(row_num+1, self.total_rows):
    #         column += 1
    #         if column < self.total_columns and pieces[column][row] == player.color:
    #             consecutive_pieces += 1
    #         else:
    #             return consecutive_pieces
    #
    # def get_se_pieces(self, pieces, player, column_num, row_num):
    #     consecutive_pieces = 0
    #     column = column_num
    #     for row in reversed(range(0, row_num)):
    #         column += 1
    #         if column < self.total_columns and pieces[column][row] == player.color:
    #             consecutive_pieces += 1
    #         else:
    #             return consecutive_pieces
    #
