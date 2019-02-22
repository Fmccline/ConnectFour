from Agents.MinimaxAgent import MinimaxAgent
from Agents.HumanAgent import HumanAgent
from PlayerSelectionView import PlayerSelectionView
from Agents.RandomAgent import RandomAgent


class PlayerFactory:

    @staticmethod
    def make_player(player_type, color, game_board_view):
        if player_type == PlayerSelectionView.HUMAN:
            return HumanAgent(color, game_board_view)
        elif player_type == PlayerSelectionView.RANDOM:
            return RandomAgent(color)
        elif player_type == PlayerSelectionView.HEURISTIC:
            return MinimaxAgent(color)
        else:
            raise Exception("Invalid player type :O " + str(player_type))

