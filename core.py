from queue import PriorityQueue
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Node:
    state : Any
    action: Optional[Any]
    parent : Optional[Any]

@dataclass
class AStarStats:
    nodes_generated = 0
    nodes_expanded = 0
    max_frontier_size = 0
    solution_depth: Optional[int] = None
    solution_cost: Optional[int] = None

def AStar():
    stats = AStarStats()
    frontier = PriorityQueue()
    seen = set()
    best_g = None #this is supposed to be a map?
    while frontier:
        pass # do the search
    return None



algorithms = {
    "AStar" : AStar
}