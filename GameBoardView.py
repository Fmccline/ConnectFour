from tkinter import Frame, Button

from GameBoard import GameBoard
from ImageHolder import ImageHolder


class GameBoardView:

    def __init__(self, window, game_board):
        self.game_board = game_board
        self.board_view = Frame(window)
        self.piece_views = []
        self.image_holder = ImageHolder()
        self.column_clicked = None
        self.new_click = False
        self.create_board()

    def create_board(self):
        num_columns, num_rows = self.game_board.get_board_size()
        for x in range(num_columns):
            piece_view_column = []
            for y in range(num_rows):
                piece = self.game_board.get_piece(x, y)
                image = self.get_piece_image(piece)
                button = Button(self.board_view, image=image)
                button.config(command=lambda column=x: self.clicked(column))
                button.grid(column=x, row=num_rows - y - 1)
                piece_view_column.append(button)
            self.piece_views.append(piece_view_column)
        self.board_view.pack()

    def get_piece_image(self, piece):
        if piece == GameBoard.EMPTY_PIECE:
            return self.image_holder.empty_piece_image
        if piece == GameBoard.BLACK_PIECE:
            return self.image_holder.black_piece_image
        if piece == GameBoard.RED_PIECE:
            return self.image_holder.red_piece_image
        raise Exception("Invalid piece type " + str(piece) + " in get_piece_image")

    def clicked(self, column):
        self.column_clicked = column
        self.new_click = True

    def get_clicked_column(self):
        if self.new_click is True:
            self.new_click = False
            return self.column_clicked
        else:
            return None

    def update_board(self):
        num_columns, num_rows = self.game_board.get_board_size()
        for x in range(num_columns):
            for y in range(num_rows):
                piece = self.game_board.get_piece(x, y)
                image = self.get_piece_image(piece)
                button = self.piece_views[x][y]
                button.config(image=image)
