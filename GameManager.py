from tkinter import Tk, Label, messagebox, Button
from GameBoard import GameBoard
from GameBoardView import GameBoardView
from Game import Game
from Player import Player
from PlayerFactory import PlayerFactory
from PlayerSelectionView import PlayerSelectionView
from WinnerCalculator import WinnerCalculator


class GameManager:
    NUM_COLUMNS = 7
    NUM_ROWS = 6

    def __init__(self):
        self.window = self.make_window()
        self.make_title_view()
        self.red_player_selection = PlayerSelectionView(self.window, Player.RED_PLAYER)
        self.black_player_selection = PlayerSelectionView(self.window, Player.RED_PLAYER)
        self.start_button = Button(self.window, text='New Game', command=self.new_game)
        self.start_button.pack()
        self.game_board = GameBoard(self.NUM_COLUMNS, self.NUM_ROWS)
        self.game_board_view = GameBoardView(self.window, self.game_board)
        self.new_game = False
        self.game = None
        self.winner_calculator = WinnerCalculator(self.game_board)

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

    def main_loop(self):
        game_board = self.game_board
        game_board_view = self.game_board_view
        window = self.window
        while True:
            if self.new_game:
                self.new_game = False
                self.game = self.start_game()
            if self.game is not None:
                current_player = self.game.current_player
                self.game.take_turn()
                game_board_view.update_board()
                if self.winner_calculator.is_winner(current_player, game_board):
                    title = 'Winner!'
                    message = current_player.name + " wins!"
                    messagebox.showinfo(title, message)
                    game_board.reset_board()
            window.update_idletasks()
            window.update()

    def start_game(self):
        red_player_type = self.red_player_selection.get_player_from_selection()
        black_player_type = self.black_player_selection.get_player_from_selection()
        red_player = PlayerFactory.make_player(red_player_type, Player.RED_PLAYER, self.game_board_view)
        black_player = PlayerFactory.make_player(black_player_type, Player.BLACK_PLAYER, self.game_board_view)
        game = Game(self.game_board, red_player, black_player)
        return game

