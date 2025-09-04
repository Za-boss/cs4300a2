import array
from dataclasses import dataclass
from typing import Optional
@dataclass(frozen=True)
class puzzleState:
    puzzle: tuple
    cost: Optional[int] = 0
def nullHeuristic(state : puzzleState, goalState: puzzleState):
    return 0
def misplacedHeuristic(state : puzzleState, goalState: puzzleState):
    pass
def manhattanHeuristic(state: puzzleState, goalState: puzzleState):
    pass
heuristics = {
    "null" : nullHeuristic,
    "misplaced" : misplacedHeuristic,
    "manhattan" : manhattanHeuristic
}

moves = {
    "move up": (0, -1),
    "move down": (0, 1),
    "move right": (1, 0),
    "move left" : (-1, 0)
}

class puzzleProblem:
    def __init__(self, initialState : puzzleState, goalState : puzzleState, heuristic):
        self.initialState = initialState
        self.goalState = goalState
        self.heuristic = heuristic
    def Actions(self, state: puzzleState):
        nullIndex = state.puzzle.index(0)
        row, col = divmod(nullIndex, 3)
        availableMoves = []
        for move, (x, y) in moves.items():
            newRow, newCol = row + x, col + y
            if 0 <= newRow < 3 and 0 <= newCol < 3:
                availableMoves.append(move)
        return availableMoves
    def Transition(self, state: puzzleState, action):
        nullIndex = state.puzzle.index(0)
        row, col = divmod(nullIndex, 3)
        newState = array.array("i", state.puzzle)
        newRow, newCol = row + moves[action][0], col + moves[action][1]
        newIndex = newRow  * 3 + newCol
        newState[nullIndex], newState[newIndex] = newState[newIndex], newState[nullIndex]
        return puzzleState(tuple(newState), state.cost + 1)
    def GoalTest(self, state: puzzleState):
        return(state.puzzle == self.goalState.puzzle)
    def StepCost(self, state: puzzleState, action, newState: puzzleState):
        return (newState.cost)
    def CallHeuristic(self, state : puzzleState):
        return self.heuristic(state, self.goalState)
