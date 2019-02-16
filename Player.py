from GameBoard import GameBoard


class Player:
    RED_PLAYER = GameBoard.RED_PIECE
    BLACK_PLAYER = GameBoard.BLACK_PIECE

    def __init__(self, color, game_board):
        self.color = color
        self.game_board = game_board
        self.name = 'RED' if color == self.RED_PLAYER else 'BLACK'
        pass

    def take_turn(self, game_board):
        pass
