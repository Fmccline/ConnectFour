import copy
import time
import random

from GameManager import GameManager
from MinimaxAgent import MinimaxAgent
from Agent import Agent
from GameBoard import GameBoard
from HeuristicEvaluator import HeuristicEvaluator
from WinnerCalculator import WinnerCalculator


class TimingTest:

    MAX_MOVES = 20

    def __init__(self, num_columns, num_rows):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.winner_calculator = WinnerCalculator()

    def print_evaluations_per_second(self, num_boards, iterations):
        print("Running evaluations per second test")
        total_evaluations = num_boards * iterations
        evaluation_time = self.get_move_evaluations_per_second(num_boards, iterations)
        print(f"Evaluations per second: {evaluation_time} (over {total_evaluations} total evaluations)")

    def print_agent_evaluations_per_second(self, num_boards):
        print("Running agent evaluations per second test")
        evaluations_per_second = self.get_agent_evaluations_per_second(num_boards)
        total_turns = num_boards
        print(f"Agent evaluations per second: {evaluations_per_second} (over {total_turns} total evaluations)")

    def print_games_per_second(self, num_games):
        print("Running games per second test")
        evaluations_per_second = self.get_games_run_per_second(num_games)
        total_games = num_games
        print(f"Games per second: {evaluations_per_second} (over {total_games} total games)")

    def get_move_evaluations_per_second(self, num_boards, iterations):
        game_boards = self.create_random_game_boards(num_boards)
        color = Agent.RED_PLAYER
        evaluator = HeuristicEvaluator()
        t0 = time.time()
        for iteration in range(iterations):
            for game_board in game_boards:
                evaluator.get_board_evaluation(game_board, color)
        t1 = time.time()
        total_time = t1 - t0
        total_evaluations = num_boards * iterations
        evaluations_per_second = total_evaluations / total_time
        return evaluations_per_second

    def create_random_game_boards(self, num_boards):
        game_boards = []
        num_moves = self.MAX_MOVES
        for game_board_num in range(num_boards):
            game_board = self.create_random_game_board(num_moves)
            game_boards.append(game_board)
            num_moves -= 1
            if num_moves == 0:
                num_moves = self.MAX_MOVES
        return game_boards

    def create_random_game_board(self, num_moves):
        game_board = GameBoard(self.num_columns, self.num_rows)
        winner_calculator = self.winner_calculator
        move_num = 0
        color = GameBoard.RED_PIECE
        while move_num < num_moves:
            moves = game_board.get_all_possible_moves()
            if not moves:
                return game_board
            new_board = copy.deepcopy(game_board)
            move = random.choice(moves)
            new_board.make_move(move, color)
            if not winner_calculator.is_winner(color, new_board):
                move_num += 1
                color = self.get_next_player_color(color)
                game_board = new_board
        return game_board

    def get_agent_evaluations_per_second(self, num_boards):
        game_boards = self.create_random_game_boards(num_boards)
        t0 = time.time()
        for game_board in game_boards:
            agent = MinimaxAgent(Agent.RED_PLAYER, game_board)
            agent.take_turn(game_board)
        t1 = time.time()
        total_time = t1 - t0
        total_turns = num_boards
        evaluations_per_second = total_turns / total_time
        return evaluations_per_second

    def get_games_run_per_second(self, num_games):
        game_board = GameBoard(self.num_columns, self.num_rows)
        game_manager = GameManager()
        red_player = MinimaxAgent(Agent.RED_PLAYER, game_board)
        black_player = MinimaxAgent(Agent.BLACK_PLAYER, game_board)
        t0 = time.time()
        game_num = 1
        for game in range(num_games):
            print(f"Playing game {game_num}")
            game_num += 1
            game_manager.start_new_game(red_player, black_player)
            while game_manager.is_playing():
                game_manager.play_turn()
        t1 = time.time()
        total_time = t1 - t0
        return num_games / total_time

    @staticmethod
    def get_next_player_color(color):
        if color == GameBoard.RED_PIECE:
            return GameBoard.BLACK_PIECE
        else:
            return GameBoard.RED_PIECE
