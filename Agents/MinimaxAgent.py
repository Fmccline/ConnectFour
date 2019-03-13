import copy

from Evaluators.ConsecutivePiecesEvaluator import ConsecutivePiecesEvaluator
from Agents.Agent import Agent
from WinnerCalculator import WinnerCalculator


class MinimaxAgent(Agent):

    def __init__(self, color):
        super().__init__(color)
        self.TURNS_AHEAD = None
        self.evaluator = None
        self.winner_calculator = WinnerCalculator()
        self.total_evaluations = 0
        self.scores = []
        self.evaluations = []

    def get_score_and_evaluations(self):
        return self.scores, self.evaluations

    def reset_scores(self):
        self.scores = []
        self.evaluations = []

    def get_move(self, game_board):
        best_move, score = self.get_best_move_and_score(game_board)
        color_name = "RED" if self.color == Agent.RED_PLAYER else "BLACK"
        print(f"{color_name}'s best move: ({best_move}, {score})")
        return best_move

    def get_best_move_and_score(self, game_board):
        self.total_evaluations = 0
        depth = self.TURNS_AHEAD * 2
        best_move, score = self.minimax(game_board, self.color, depth,
                                        ConsecutivePiecesEvaluator.NEG_INFINITY, ConsecutivePiecesEvaluator.INFINITY)
        print(f'Total Evaluations: {self.total_evaluations} out of a max {7**depth}')
        self.scores.append(score)
        self.evaluations.append(self.total_evaluations)
        return best_move, score

    def minimax(self, game_board, color, depth, alpha, beta, last_move=None, original_move=None):
        moves = game_board.get_all_possible_moves()
        if depth == 0 or not moves:
            self.total_evaluations += 1
            board_score = self.evaluator.get_board_evaluation(game_board, last_move, self.color)
            return original_move, board_score

        is_max = color == self.color
        worst_possible_score = ConsecutivePiecesEvaluator.NEG_INFINITY if is_max else ConsecutivePiecesEvaluator.INFINITY
        best_score = worst_possible_score
        best_move = None
        possible_moves = []
        for move in moves:
            new_board = game_board.make_copy()
            new_board.make_move(move, color)
            starting_move = move if original_move is None else original_move
            if self.winner_calculator.is_winner(color, new_board, move):
                player_modifier = 1 if color == self.color else -1
                board_score = ConsecutivePiecesEvaluator.WINNING_VALUE * player_modifier
                return starting_move, board_score

            new_color = Agent.RED_PLAYER if color == Agent.BLACK_PLAYER else Agent.BLACK_PLAYER
            starting_move, board_score = self.minimax(new_board, new_color, depth - 1, alpha, beta, move, starting_move)
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
