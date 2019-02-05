from GameBoard import GameBoard


class Player:
    RED_PLAYER = GameBoard.RED_PIECE
    BLACK_PLAYER = GameBoard.BLACK_PIECE

    def __init__(self, color, game_board):
        self.color = color
        self.game_board = game_board
        self.name = 'RED' if color == self.RED_PLAYER else 'BLACK'
        pass

    def take_turn(self):
        pass

    def get_played_pieces(self):
        if self.color == self.RED_PLAYER:
            played_pieces = self.game_board.get_red_pieces()
        elif self.color == self.BLACK_PLAYER:
            played_pieces = self.game_board.get_black_pieces()
        else:
            raise Exception("Player isn't Red or Black ing get_played_pieces")
        return played_pieces
