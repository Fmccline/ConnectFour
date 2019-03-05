from Agents.NumWinsAgent import NumWinsAgent
from Agents.HumanAgent import HumanAgent
from Agents.ConsecutivePiecesAgent import WholeBoardAgent
from PlayerSelectionView import PlayerSelectionView
from Agents.RandomAgent import RandomAgent


class PlayerFactory:

    @staticmethod
    def make_player(player_type, color, game_board_view):
        if player_type == PlayerSelectionView.HUMAN:
            return HumanAgent(color, game_board_view)
        if player_type == PlayerSelectionView.RANDOM:
            return RandomAgent(color)
        if player_type == PlayerSelectionView.BOARD_HEURISTIC:
            return WholeBoardAgent(color)
        if player_type == PlayerSelectionView.MOVE_HEURISTIC:
            return NumWinsAgent(color)
        else:
            raise Exception("Invalid player type :O " + str(player_type))

