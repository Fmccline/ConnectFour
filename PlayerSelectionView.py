from tkinter import Tk, StringVar, OptionMenu, Frame, LEFT, Label

from Player import Player


class PlayerSelectionView:

    HUMAN = 'Human'
    RANDOM = 'Random'
    HEURISTIC = 'Heuristic'
    PLAYER_TYPES = [HEURISTIC, HUMAN, RANDOM]

    def __init__(self, window: Tk, color):
        self.window = window
        self.color = color
        self.player_selection = StringVar(window)
        self.player_selection.set(self.PLAYER_TYPES[0])
        self.selection_frame = Frame(window)
        text = ('Red' if color == Player.RED_PLAYER else 'Black') + ' Player: '
        self.name_label = Label(self.selection_frame, text=text)
        self.name_label.pack(side=LEFT)
        self.option_menu = OptionMenu(self.selection_frame, self.player_selection, *self.PLAYER_TYPES)
        self.option_menu.pack(side=LEFT)
        self.selection_frame.pack()

    def get_player_from_selection(self):
        return self.player_selection.get()

    def get_color(self):
        return self.color

