from GameBoard import GameBoard


class Agent:
    """
    The agent returns a move given a game board
    The move can be considered the action that the Agent makes given an environment (the game board)
    The agent does not use any sensors, percepts, or actuators
    """

    RED_PLAYER = GameBoard.RED_PIECE
    BLACK_PLAYER = GameBoard.BLACK_PIECE

    def __init__(self, color):
        self.color = color
        self.name = 'RED' if color == self.RED_PLAYER else 'BLACK'
        pass

    def get_move(self, game_board):
        pass
