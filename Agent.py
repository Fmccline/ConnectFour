from GameBoard import GameBoard


class Agent:
    RED_PLAYER = GameBoard.RED_PIECE
    BLACK_PLAYER = GameBoard.BLACK_PIECE

    def __init__(self, color):
        self.color = color
        self.name = 'RED' if color == self.RED_PLAYER else 'BLACK'
        pass

    def get_move(self, game_board):
        pass
