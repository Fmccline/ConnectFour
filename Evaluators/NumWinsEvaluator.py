from ConsecutivePieceCounter import ConsecutivePieceCounter
from Evaluators.BoardEvaluator import BoardEvaluator


class NumWinsEvaluator(BoardEvaluator):

    def __init__(self):
        self.game_board = None
        self.last_move = None
        self.color = None

    def get_board_evaluation(self, game_board, last_move, color):
        self.game_board = game_board
        self.last_move = last_move
        self.color = color
        return self.get_num_wins()

    def get_num_wins(self):
        game_board = self.game_board
        last_move = self.last_move
        color = self.color
        counting_empty = True
        row = game_board.get_row(last_move)
        west = ConsecutivePieceCounter.get_west_pieces(color, last_move, row, game_board, counting_empty)
        east = ConsecutivePieceCounter.get_east_pieces(color, last_move, row, game_board, counting_empty)
        nw = ConsecutivePieceCounter.get_nw_pieces(color, last_move, row, game_board, counting_empty)
        ne = ConsecutivePieceCounter.get_ne_pieces(color, last_move, row, game_board, counting_empty)
        sw = ConsecutivePieceCounter.get_sw_pieces(color, last_move, row, game_board, counting_empty)
        se = ConsecutivePieceCounter.get_se_pieces(color, last_move, row, game_board, counting_empty)
        south = ConsecutivePieceCounter.get_vertical_pieces(color, last_move, row, game_board, counting_empty)

        vertical = 1 + south
        horizontal = west + 1 + east
        nw_se = nw + 1 + se
        ne_sw = ne + 1 + sw
        all_consecutive_pieces = [vertical, horizontal, nw_se, ne_sw]
        num_wins = 0
        for consecutive_pieces in all_consecutive_pieces:
            if consecutive_pieces >= 4:
                num_wins += consecutive_pieces - 3
        return num_wins
