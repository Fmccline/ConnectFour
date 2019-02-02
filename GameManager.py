from GameBoard import GameBoard


class GameManager:
    NO_PLAYER = GameBoard.EMPTY_PIECE
    RED_PLAYER = GameBoard.RED_PIECE
    BLACK_PLAYER = GameBoard.BLACK_PIECE

    def __init__(self, game_board: GameBoard, red_player, black_player):
        self.game_board = game_board
        self.red_player = red_player
        self.black_player = black_player
        self.current_turn = self.RED_PLAYER

    def take_turn(self):
        current_player = self.red_player if self.current_turn == self.RED_PLAYER else self.black_player
        turn_taken = current_player.take_turn(self.game_board)
        if turn_taken is True:
            self.current_turn = self.BLACK_PLAYER if self.current_turn == self.RED_PLAYER else self.RED_PLAYER
            print("Current turn: " + str(self.current_turn))

    def is_winner(self):
        pieces = self.game_board.get_pieces()
        if self.is_vertical_win(pieces):
            print("Vertical")
            return True
        elif self.is_horizontal_win(pieces):
            print("Horizontal")
            return True
        else:
            return False

    def is_vertical_win(self, pieces):
        last_piece = None
        for column in pieces:
            consecutive_pieces = 0
            for piece in column:
                if piece == GameBoard.EMPTY_PIECE:
                    break
                elif last_piece == piece:
                    consecutive_pieces += 1
                    if consecutive_pieces >= 3:
                        return True
                else:
                    consecutive_pieces = 0
                last_piece = piece
        return False

    def is_horizontal_win(self, pieces):
        total_pieces = self.game_board.played_pieces
        last_piece = None
        total_rows = len(pieces[0])
        total_columns = len(pieces)
        for row_num in range(total_rows):
            for col_num in range(total_columns):
                piece = pieces[col_num][row_num]
                if piece == last_piece and piece != GameBoard.EMPTY_PIECE:
                    consecutive_pieces += 1
                    if consecutive_pieces >= 3:
                        return True
                else:
                    consecutive_pieces = 0
                if piece != GameBoard.EMPTY_PIECE:
                    total_pieces -= 1
                    if total_pieces <= 0:
                        return False
                last_piece = piece
        return False
