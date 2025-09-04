from queue import PriorityQueue
from dataclasses import dataclass
from typing import Any, Optional
import itertools

counter = itertools.count()

@dataclass
class Node:
    state : Any
    action: Optional[Any] = None
    parent : Optional[Any] = None

@dataclass
class AStarStats:
    nodesGenerated = 0
    nodesExpanded = 0
    maxFrontierSize = 0
    solutionDepth: Optional[int] = None
    solutionCost: Optional[int] = None

def AStar(problem):
    stats = AStarStats()
    frontier = PriorityQueue()
    start = problem.initialState
    g0 = 0
    f0 = g0 + problem.CallHeuristic(start)
    frontier.put((f0, next(counter), Node(problem.initialState)))
    best_g = {start : g0} 
    while not frontier.empty():
        stats.maxFrontierSize = max(stats.maxFrontierSize, frontier.qsize())
        f, _, node = frontier.get()
        stats.nodesExpanded += 1
        g = best_g[node.state] 
        if problem.GoalTest(node.state):
            path = []
            stats.solutionCost = g
            while node:
                path.append(node)
                node = node.parent
            stats.solutionDepth = len(path) - 1
            return (path[::-1], stats)
        for action in problem.Actions(node.state):
            newState = problem.Transition(node.state, action)
            gPrime = g + problem.StepCost(node.state, action, newState)
            fPrime =  gPrime + problem.CallHeuristic(newState)
            if newState not in best_g or gPrime < best_g[newState]:
                best_g[newState] = gPrime
                frontier.put((fPrime, next(counter), Node(newState, action, node)))
                stats.nodesGenerated += 1
    return (None, stats)
algorithms = {
    "AStar" : AStar
}