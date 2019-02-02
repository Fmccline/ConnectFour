from tkinter import Tk, Label
from GameBoard import GameBoard
from GameBoardView import GameBoardView
from GameManager import GameManager
from HumanPlayer import HumanPlayer

NUM_COLUMNS = 7
NUM_ROWS = 6


def main():
    print("starting")
    window = make_window()
    game_board = GameBoard(NUM_COLUMNS, NUM_ROWS)
    game_board_view = GameBoardView(window, game_board)
    red_player = HumanPlayer(GameManager.RED_PLAYER, game_board_view)
    black_player = HumanPlayer(GameManager.BLACK_PLAYER, game_board_view)
    game_manager = GameManager(game_board, red_player, black_player)
    while True:
        if not game_manager.is_winner():
            game_manager.take_turn()
        else:
            game_board.print_board()
            game_board.reset_board()
        game_board_view.update_board()
        window.update_idletasks()
        window.update()


def make_window():
    window = Tk()
    window.title("Connect Four")
    window.geometry('640x400')
    title_label = Label(window, text='Connect FooooR')
    title_label.pack()
    return window


if __name__ == '__main__':
    main()
