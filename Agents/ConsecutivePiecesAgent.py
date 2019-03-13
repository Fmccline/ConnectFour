from Agents.MinimaxAgent import MinimaxAgent
from Evaluators.ConsecutivePiecesEvaluator import ConsecutivePiecesEvaluator


class ConsecutivePiecesAgent(MinimaxAgent):

    def __init__(self, color):
        super().__init__(color)
        self.TURNS_AHEAD = 3
        self.evaluator = ConsecutivePiecesEvaluator()
