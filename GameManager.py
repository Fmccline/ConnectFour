from tkinter import Tk, Label, messagebox
from GameBoard import GameBoard
from GameBoardView import GameBoardView
from Game import Game
from Player import Player
from HumanPlayer import HumanPlayer


class GameManager:
    NUM_COLUMNS = 7
    NUM_ROWS = 6

    def __init__(self):
        self.window = self.make_window()
        self.game_board = GameBoard(self.NUM_COLUMNS, self.NUM_ROWS)
        self.game_board_view = GameBoardView(self.window, self.game_board)
        self.red_player = HumanPlayer(Player.RED_PLAYER, self.game_board_view)
        self.black_player = HumanPlayer(Player.BLACK_PLAYER, self.game_board_view)
        self.game = Game(self.game_board, self.red_player, self.black_player)

    def make_window(self):
        window = Tk()
        window.title("Connect Four")
        window.geometry('640x400')
        title_label = Label(window, text='Connect FooooR')
        title_label.pack()
        return window

    def main_loop(self):
        game = self.game
        game_board = self.game_board
        game_board_view = self.game_board_view
        window = self.window
        while True:
            current_player = game.current_player
            game.take_turn()
            game_board_view.update_board()
            window.update_idletasks()
            window.update()
            if game.is_winner(current_player):
                title = 'Winner!'
                message = current_player.name + " wins!"
                messagebox.showinfo(title, message)
                game_board.reset_board()
