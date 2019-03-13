from Agents.NumWinsAgent import NumWinsAgent
from Agents.HumanAgent import HumanAgent
from Agents.ConsecutivePiecesAgent import ConsecutivePiecesAgent
from Agents.SmartRandomAgent import SmartRandomAgent
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
            return ConsecutivePiecesAgent(color)
        if player_type == PlayerSelectionView.MOVE_HEURISTIC:
            return NumWinsAgent(color)
        if player_type == PlayerSelectionView.SMART_RANDOM:
            return SmartRandomAgent(color)
        else:
            raise Exception("Invalid player type :O " + str(player_type))

