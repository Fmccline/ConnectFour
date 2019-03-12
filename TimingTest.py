import copy
import time
import random

from Agents.NumWinsAgent import NumWinsAgent
from GameManager import GameManager
from Agents.Agent import Agent
from GameBoard import GameBoard
from Evaluators.ConsecutivePiecesEvaluator import ConsecutivePiecesEvaluator
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

    def print_seconds_per_agent_move(self, num_boards):
        print("Running seconds per agent move test")
        seconds_per_evaluation = self.get_agent_evaluations_per_second(num_boards)
        print(f"Seconds per agent evaluation: {seconds_per_evaluation} (over {num_boards} total evaluations)")

    def print_games_per_second(self, num_games):
        print("Running games per second test")
        evaluations_per_second = self.get_games_run_per_second(num_games)
        total_games = num_games
        print(f"Games per second: {evaluations_per_second} (over {total_games} total games)")

    def print_board_creations_per_second(self, num_boards):
        print("Running boards per second test")
        boards_per_second = self.get_board_creations_per_second(num_boards)
        print(f"Board creations per second: {boards_per_second} over {num_boards} total boards")

    def get_move_evaluations_per_second(self, num_boards, iterations):
        game_boards = self.create_random_game_boards(num_boards)
        color = Agent.RED_PLAYER
        evaluator = ConsecutivePiecesEvaluator()
        t0 = time.time()
        for iteration in range(iterations):
            for last_move, game_board in game_boards.items():
                evaluator.get_board_evaluation(game_board, last_move, color)
        t1 = time.time()
        total_time = t1 - t0
        total_evaluations = num_boards * iterations
        evaluations_per_second = total_evaluations / total_time
        return evaluations_per_second

    def create_random_game_boards(self, num_boards):
        game_boards = {}
        num_moves = self.MAX_MOVES
        for game_board_num in range(num_boards):
            game_board, last_move = self.create_random_game_board(num_moves)
            game_boards[last_move] = game_board
            num_moves -= 1
            if num_moves == 0:
                num_moves = self.MAX_MOVES
        return game_boards

    def create_random_game_board(self, num_moves):
        game_board = GameBoard(self.num_columns, self.num_rows)
        winner_calculator = self.winner_calculator
        move_num = 0
        color = GameBoard.RED_PIECE
        last_move = None
        while move_num < num_moves:
            moves = game_board.get_all_possible_moves()
            if not moves:
                return game_board
            new_board = copy.deepcopy(game_board)
            move = random.choice(moves)
            new_board.make_move(move, color)
            last_move = move
            if not winner_calculator.is_winner(color, new_board, move):
                move_num += 1
                color = self.get_next_player_color(color)
                game_board = new_board
        return game_board, last_move

    def get_agent_evaluations_per_second(self, num_boards):
        game_boards = self.create_random_game_boards(num_boards)
        t0 = time.time()
        for game_board in game_boards.values():
            agent = NumWinsAgent(Agent.RED_PLAYER)
            agent.get_move(game_board)
        t1 = time.time()
        total_time = t1 - t0
        total_turns = num_boards
        evaluations_per_second = total_time / total_turns
        return evaluations_per_second

    def get_games_run_per_second(self, num_games):
        game_manager = GameManager()
        red_player = NumWinsAgent(Agent.RED_PLAYER)
        black_player = NumWinsAgent(Agent.BLACK_PLAYER)
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

    def get_board_creations_per_second(self, num_boards):
        boards = []
        board = GameBoard(self.num_columns, self.num_rows)
        # board = [GameBoard.EMPTY_PIECE] * self.num_columns * self.num_rows
        t0 = time.time()
        for _ in range(num_boards):
            new_board = copy.copy(board)
            boards.append(new_board)
        t1 = time.time()
        total_time = t1 - t0
        return num_boards / total_time

    @staticmethod
    def get_next_player_color(color):
        if color == GameBoard.RED_PIECE:
            return GameBoard.BLACK_PIECE
        else:
            return GameBoard.RED_PIECE
