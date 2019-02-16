from tkinter import Button, Label, Tk, messagebox

from GameBoardView import GameBoardView
from GameManager import GameManager
from Player import Player
from PlayerFactory import PlayerFactory
from PlayerSelectionView import PlayerSelectionView


class GameManagerView:
    NUM_COLUMNS = 7
    NUM_ROWS = 6

    def __init__(self):
        self.window = self.make_window()
        self.make_title_view()
        self.red_player_selection = PlayerSelectionView(self.window, Player.RED_PLAYER)
        self.black_player_selection = PlayerSelectionView(self.window, Player.BLACK_PLAYER)
        self.start_button = Button(self.window, text='New Game', command=self.new_game)
        self.start_button.pack()
        self.current_turn_view = Label(self.window, text="Turn: N/A")
        self.current_turn_view.pack()
        self.game_manager = GameManager()
        self.game_board_view = GameBoardView(self.window, self.game_manager.game_board)
        self.new_game = False

    def make_window(self):
        window = Tk()
        window.title("Connect Four")
        window.geometry('960x600')
        return window

    def make_title_view(self):
        title_label = Label(self.window, text='Connect FooooR')
        title_label.pack()

    def new_game(self):
        self.new_game = True

    def get_player_selections(self):
        red_player_type = self.red_player_selection.get_player_from_selection()
        black_player_type = self.black_player_selection.get_player_from_selection()
        red_player = PlayerFactory.make_player(red_player_type, Player.RED_PLAYER, self.game_board_view)
        black_player = PlayerFactory.make_player(black_player_type, Player.BLACK_PLAYER, self.game_board_view)
        return red_player, black_player

    def main_loop(self):
        game_board_view = self.game_board_view
        game_manager = self.game_manager
        window = self.window
        while True:
            if self.new_game:
                self.new_game = False
                red_player, black_player = self.get_player_selections()
                game_manager.start_new_game(red_player, black_player)
            if game_manager.is_playing():
                current_player = game_manager.get_current_player()
                game_manager.play_turn()
                game_board_view.update_board()
                if not game_manager.is_playing():
                    if game_manager.is_draw():
                        title = 'Draw!'
                        message = "It's a draw!"
                    else:
                        winner = game_manager.get_winner()
                        title = 'Winner!'
                        message = winner.name + " wins!"
                    messagebox.showinfo(title, message)
                else:
                    self.current_turn_view.config(text="Turn: " + current_player.name)
            window.update_idletasks()
            window.update()
