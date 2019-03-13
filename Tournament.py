from Agents.Agent import Agent
from GameManager import GameManager


class Tournament:

    def __init__(self, player_1, player_2, num_games):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_wins = []
        self.num_games = num_games
        self.game_manager = GameManager()

    def play_tournament(self):
        self.player_wins = []
        red_player = self.player_1
        black_player = self.player_2
        for game in range(self.num_games):
            num_moves = 0
            if red_player == self.player_1:
                red_player = self.player_2
                black_player = self.player_1
            else:
                red_player = self.player_1
                black_player = self.player_2
            red_player.color = Agent.RED_PLAYER
            black_player.color = Agent.BLACK_PLAYER
            self.game_manager.start_new_game(red_player, black_player)
            while self.game_manager.is_playing():
                self.game_manager.play_turn()
                num_moves += 1
            winner = self.game_manager.get_winner()
            if winner is not None:
                winner_name = 'Player 1'
                if winner == self.player_2:
                    winner_name = 'Player 2'
                color = "RED" if winner.color == Agent.RED_PLAYER else "BLACK"
                agent_type = str(type(winner))
            else:
                winner_name = 'Draw'
                color = "-"
                agent_type = '-'
            self.player_wins.append([winner_name, color, num_moves, agent_type])

    def get_player_wins(self):
        return self.player_wins
