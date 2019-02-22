from Agent import Agent


class HumanAgent(Agent):

    def __init__(self, color, game_board_view):
        super().__init__(color)
        self.game_board_view = game_board_view

    def get_move(self, game_board):
        column = self.game_board_view.get_clicked_column()
        return column


