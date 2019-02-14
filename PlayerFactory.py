from HeuristicPlayer import HeuristicPlayer
from HumanPlayer import HumanPlayer
from PlayerSelectionView import PlayerSelectionView
from RandomPlayer import RandomPlayer


class PlayerFactory:

    @staticmethod
    def make_player(player_type, color, game_board_view):
        game_board = game_board_view.game_board
        if player_type == PlayerSelectionView.HUMAN:
            return HumanPlayer(color, game_board_view)
        elif player_type == PlayerSelectionView.RANDOM:
            return RandomPlayer(color, game_board)
        elif player_type == PlayerSelectionView.HEURISTIC:
            return HeuristicPlayer(color, game_board)
        else:
            raise Exception("Invalid player type :O " + str(player_type))

