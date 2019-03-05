from Agents.MinimaxAgent import MinimaxAgent
from Evaluators.ConsecutivePiecesEvaluator import ConsecutivePiecesEvaluator


class WholeBoardAgent(MinimaxAgent):

    def __init__(self, color):
        super().__init__(color)
        self.evaluator = ConsecutivePiecesEvaluator()
