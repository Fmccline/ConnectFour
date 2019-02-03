from GameBoard import GameBoard


class Game:

    def __init__(self, game_board: GameBoard, red_player, black_player):
        self.game_board = game_board
        self.red_player = red_player
        self.black_player = black_player
        self.current_player = red_player

    def take_turn(self):
        turn_taken = self.current_player.take_turn()
        if turn_taken is True:
            self.current_player = self.black_player if self.current_player == self.red_player else self.red_player
            print("Current turn: " + str(self.current_player))

    def is_winner(self, player):
        pieces = self.game_board.get_pieces()
        if self.is_vertical_win(pieces, player):
            print("Vertical")
            return True
        elif self.is_horizontal_win(pieces, player):
            print("Horizontal")
            return True
        else:
            return False

    def is_vertical_win(self, pieces, player):
        played_pieces = player.get_played_pieces()
        for column in pieces:
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

    def is_horizontal_win(self, pieces, player):
        played_pieces = player.get_played_pieces()
        total_columns, total_rows = self.game_board.get_board_size()
        for row_num in range(total_rows):
            consecutive_pieces = 0
            for col_num in range(total_columns):
                piece = pieces[col_num][row_num]
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
