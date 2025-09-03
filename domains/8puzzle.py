class puzzleState:
    def __init__(self):
        self
def nullHeuristic(state : puzzleState):
    return 0
def misplacedHeuristic(state : puzzleState):
    pass
def manhattanHeuristic(state: puzzleState):
    pass
heuristics = {
    "null" : nullHeuristic,
    "misplaced" : misplacedHeuristic,
    "manhattan" : manhattanHeuristic
}
class puzzleProblem:
    def __init__(self, initialState : puzzleState, goalState : puzzleState, heuristic):
        self.initialState = initialState
        self.goalState = goalState
    def Actions(self, state: puzzleState):
        pass
    def Transition(self, state: puzzleState, action):
        pass
    def GoalTest(self, state: puzzleState):
        pass
    def StepCost(self, state: puzzleState, action, newState: puzzleState):
        pass
