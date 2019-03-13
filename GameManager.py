from GameBoard import GameBoard
from Game import Game


class GameManager:
    NUM_COLUMNS = 7
    NUM_ROWS = 6

    def __init__(self):
        self.game_board = GameBoard(self.NUM_COLUMNS, self.NUM_ROWS)
        self.playing = False
        self.game = None
        self.current_player = None
        self.winner = None

    def start_new_game(self, red_player, black_player):
        self.game_board.reset_board()
        self.game = Game(self.game_board, red_player, black_player)
        self.current_player = self.game.current_player
        self.playing = True
        self.winner = None

    def play_turn(self):
        if not self.playing:
            return

        self.winner = self.game.take_turn()
        if self.winner is not None:
            self.playing = False
        elif self.game_board.is_full_board():
            self.playing = False

    def is_playing(self):
        return self.playing

    def get_winner(self):
        return self.winner

    def is_draw(self):
        return self.winner is None

    def get_current_player(self):
        return self.game.current_player
