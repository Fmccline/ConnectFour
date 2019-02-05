from HumanPlayer import HumanPlayer
from PlayerSelectionView import PlayerSelectionView


class PlayerFactory:

    @staticmethod
    def make_player(player_type, color, game_board_view):
        if player_type == PlayerSelectionView.HUMAN:
            return HumanPlayer(color, game_board_view)
        elif player_type == PlayerSelectionView.RANDOM:
            raise Exception("Random player not implemented yet :(")
        else:
            raise Exception("Invalid player type :O " + str(player_type))

