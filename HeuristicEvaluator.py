from GameBoard import GameBoard
from collections import deque
import math


class HeuristicEvaluator:

    INFINITY = math.inf
    NEG_INFINITY = -INFINITY

    WINNING_VALUE = 100000000000000

    def __init__(self):
        self.color = None
        self.pieces = None
        self.num_columns = None
        self.num_rows = None
        self.consecutive_pieces = 0
        self.player_pieces = 0
        self.last_player_piece = None
        self.pieces_queue = deque()

    def get_board_evaluation(self, game_board, color):
        self.pieces = game_board.get_pieces()
        self.color = color
        self.num_columns, self.num_rows = game_board.get_board_size()
        self.reset_consecutive_pieces()
        vertical_evaluations = self.get_vertical_evaluations()
        horizontal_evaluations = self.get_horizontal_evaluations()
        diagonal_evaluations = self.get_diagonal_evaluations()
        return vertical_evaluations + horizontal_evaluations + diagonal_evaluations

    def reset_consecutive_pieces(self):
        self.consecutive_pieces = 0
        self.player_pieces = 0
        self.pieces_queue = deque()
        self.last_player_piece = None

    def get_vertical_evaluations(self):
        score = 0
        for column in range(self.num_columns):
            self.reset_consecutive_pieces()
            for row in range(self.num_rows):
                board_score = self.get_board_score(column, row)
                score += board_score
        return score

    def get_horizontal_evaluations(self):
        score = 0
        for row in range(self.num_rows):
            self.reset_consecutive_pieces()
            for column in range(self.num_columns):
                board_score = self.get_board_score(column, row)
                score += board_score
        return score

    def get_diagonal_evaluations(self):
        score = 0
        # Get northeast diagonals
        # start at 4th column, go backwards
        # when column is 0, go through the first 3 rows
        column = 4
        row = 0
        while column > 0:
            board_score = self.get_north_east_diagonal_score(column, row)
            score += board_score
            column -= 1
        while row < 3:
            board_score = self.get_north_east_diagonal_score(column, row)
            score += board_score
            row += 1
        # Get northwest diagonals
        # Start at 4th column go to end
        # When column is at end, go through first 3 rows
        column = 4
        row = 0
        while column < self.num_columns - 1:
            board_score = self.get_north_west_diagonal_score(column, row)
            score += board_score
            column += 1
        while row < 3:
            board_score = self.get_north_west_diagonal_score(column, row)
            score += board_score
            row += 1
        return score

    def get_north_east_diagonal_score(self, column, row):
        score = 0
        self.reset_consecutive_pieces()
        current_row = row
        for current_column in range(column, self.num_columns):
            board_score = self.get_board_score(current_column, current_row)
            score += board_score
            current_row += 1
            if current_row >= self.num_rows:
                break
        return score

    def get_north_west_diagonal_score(self, column, row):
        score = 0
        self.reset_consecutive_pieces()
        current_row = row
        for current_column in reversed(range(column+1)):
            board_score = self.get_board_score(current_column, current_row)
            score += board_score
            current_row -= 1
            if current_row >= self.num_rows:
                break
        return score

    def get_board_score(self, column, row):
        score = 0
        piece = self.pieces[column][row]
        self.pieces_queue.append(piece)
        last_player_piece = self.last_player_piece
        if piece == last_player_piece or piece == GameBoard.EMPTY_PIECE:
            if piece == last_player_piece:
                self.player_pieces += 1
            self.consecutive_pieces += 1
            if self.consecutive_pieces == 4:
                if last_player_piece == self.color or last_player_piece is None:
                    player_modifier = 1
                else:
                    player_modifier = -1
                if self.player_pieces == 4:
                    return self.WINNING_VALUE * player_modifier  # Won the game
                else:
                    score += 2 ** self.player_pieces * player_modifier
                first_piece = self.pieces_queue.popleft()
                if first_piece == last_player_piece:
                    self.player_pieces -= 1
                self.consecutive_pieces -= 1
        else:
            self.consecutive_pieces = 1
            self.player_pieces = 1
            self.last_player_piece = piece
        return score
