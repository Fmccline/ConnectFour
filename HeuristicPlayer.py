import copy

from HeuristicEvaluator import HeuristicEvaluator
from Player import Player
from WinnerCalculator import WinnerCalculator


class HeuristicPlayer(Player):

    TURNS_AHEAD = 3

    def __init__(self, color, game_board):
        super().__init__(color, game_board)
        self.num_columns, self.num_rows = self.game_board.get_board_size()
        self.evaluator = HeuristicEvaluator(self.game_board, color)
        self.winner_calculator = WinnerCalculator()

    def take_turn(self, game_board):
        self.game_board = game_board
        best_move, score = self.get_best_move_and_score()
        game_board.make_move(best_move, self.color)
        print(f"Best move: ({best_move}, {score})")
        return True

    def get_best_move_and_score(self):
        depth = self.TURNS_AHEAD * 2
        return self.minimax(self.game_board, self.color, depth,
                            HeuristicEvaluator.NEG_INFINITY, HeuristicEvaluator.INFINITY)

    def minimax(self, game_board, color, depth, alpha, beta, original_move=None):
        moves = game_board.get_all_possible_moves()
        if depth == 0 or not moves:
            board_score = self.evaluator.get_board_evaluation(game_board, color)
            return original_move, board_score

        is_max = color == self.color
        worst_possible_score = HeuristicEvaluator.NEG_INFINITY if is_max else HeuristicEvaluator.INFINITY
        best_score = worst_possible_score
        best_move = None
        possible_moves = []
        for move in moves:
            new_board = copy.deepcopy(game_board)
            new_board.make_move(move, color)
            starting_move = move if original_move is None else original_move
            if self.winner_calculator.is_winner(color, new_board):
                player_modifier = 1 if color == self.color else -1
                board_score = HeuristicEvaluator.WINNING_VALUE * player_modifier
                return starting_move, board_score

            new_color = Player.RED_PLAYER if color == Player.BLACK_PLAYER else Player.BLACK_PLAYER
            starting_move, board_score = self.minimax(new_board, new_color, depth - 1, alpha, beta, starting_move)
            possible_moves.append((starting_move, board_score))
            if is_max and board_score > best_score:
                best_score = board_score
                best_move = starting_move
                alpha = max(alpha, best_score)
            elif not is_max and board_score < best_score:
                best_score = board_score
                best_move = starting_move
                beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_move, best_score


