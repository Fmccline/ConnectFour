from Agents.MinimaxAgent import MinimaxAgent
from Evaluators.NumWinsEvaluator import NumWinsEvaluator


class NumWinsAgent(MinimaxAgent):

    def __init__(self, color):
        super().__init__(color)
        self.TURNS_AHEAD = 4
        self.evaluator = NumWinsEvaluator()
