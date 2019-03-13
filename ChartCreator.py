import csv
import time
from Agents.Agent import Agent
from Agents.NumWinsAgent import NumWinsAgent
from GameManager import GameManager


class ChartCreator:

    def __init__(self):
        self.game_manager = GameManager()
        self.red_player = NumWinsAgent(Agent.RED_PLAYER)
        self.black_player = NumWinsAgent(Agent.BLACK_PLAYER)
        self.total_time = None

    def make_charts(self, num_games, file_name):
        self.total_time = 0
        game_num = 0
        while game_num < num_games:
            self.black_player.reset_scores()
            self.red_player.reset_scores()
            game_num += 1
            out_file = f"game_{game_num}_{file_name}"
            game_time = self.play_game()
            self.write_evaluations(out_file, game_time)
            self.total_time += game_time
        print(f"Total time over {num_games} total games: {self.total_time}")

    def play_game(self):
        start_time = time.time()
        game_manager = self.game_manager
        game_manager.start_new_game(self.red_player, self.black_player)
        while game_manager.is_playing():
            game_manager.play_turn()
        end_time = time.time()
        total_time = end_time - start_time
        return total_time

    def write_evaluations(self, file_name, game_time):
        red_scores, red_evaluations = self.red_player.get_score_and_evaluations()
        black_scores, black_evaluations = self.black_player.get_score_and_evaluations()
        if len(red_scores) != len(red_evaluations) or len(black_scores) != len(black_evaluations):
            raise Exception("Scores and evaluations don't match!")
        as_csv = [['Total time', game_time], ["Turn", "Red Score", "Black Score", "Turn", "Red Evaluations", "Black Evaluations"]]
        for index in range(len(red_scores)):
            red_score = red_scores[index]
            red_evaluation = red_evaluations[index]
            black_score = black_scores[index]
            black_evaluation = black_evaluations[index]
            row = [index, red_score, black_score, index, red_evaluation, black_evaluation]
            as_csv.append(row)
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in as_csv:
                csv_writer.writerow(row)
