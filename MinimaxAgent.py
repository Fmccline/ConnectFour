import copy

from HeuristicEvaluator import HeuristicEvaluator
from Agent import Agent
from WinnerCalculator import WinnerCalculator


class MinimaxAgent(Agent):

    TURNS_AHEAD = 3

    def __init__(self, color):
        super().__init__(color)
        self.evaluator = HeuristicEvaluator()
        self.winner_calculator = WinnerCalculator()

    def get_move(self, game_board):
        best_move, score = self.get_best_move_and_score(game_board)
        print(f"Best move: ({best_move}, {score})")
        return best_move

    def get_best_move_and_score(self, game_board):
        depth = self.TURNS_AHEAD * 2
        return self.minimax(game_board, self.color, depth,
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
            if self.winner_calculator.is_winner(color, new_board, move):
                player_modifier = 1 if color == self.color else -1
                board_score = HeuristicEvaluator.WINNING_VALUE * player_modifier
                return starting_move, board_score

            new_color = Agent.RED_PLAYER if color == Agent.BLACK_PLAYER else Agent.BLACK_PLAYER
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


