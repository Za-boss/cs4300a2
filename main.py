import random
import core
import argparse
import domains.eightPuzzle
def countInversions(state):
    tiles = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions
def isSolvable(state):
    return countInversions(state) % 2 == 0 
def generatePuzzles(number, goalState : domains.eightPuzzle.puzzleState):
    seen = set()
    while (len(seen) < number):
        state = list(goalState.puzzle)
        random.shuffle(state)
        state = tuple(state)
        if isSolvable(state) and state not in seen:
            state = domains.eightPuzzle.puzzleState(state)
            seen.add(state)
    return list(seen)
def printStats(runID, configurationId, stats, heuristic):
    print(
        f"{runID},"
        f"{configurationId},"
        f"{heuristic},"
        f"{stats.nodesExpanded},"
        f"{stats.nodesGenerated},"
        f"{stats.maxFrontierSize},"
        f"{stats.solutionCost},"
        f"{stats.solutionDepth}"
    )
def main():
    goalState = domains.eightPuzzle.puzzleState((
            0, 1, 2,
            3, 4, 5,
            6, 7, 8
        )
    )
    parser = argparse.ArgumentParser(description="Agent runner")
    parser.add_argument('--algo', type=str, required=False, default="AStar", choices=core.algorithms.keys())
    parser.add_argument('--configurationCount', '--cc', type=int, required=False, default=1)
    parser.add_argument('--heuristic', '--h', type=str, required=False, default='null', choices=list(domains.eightPuzzle.heuristics.keys()) + ["all"])
    parser.add_argument('--seed', '--s', type=int, required=False)
    args = parser.parse_args()
    algorithm = core.algorithms[args.algo]
    configurationCount = args.configurationCount
    heuristic = args.heuristic
    seed = args.seed
    if not seed:
        seed = random.randrange(1000000)
    random.seed(seed)
    print(f"Configuration Seed: {seed}")
    configurations = generatePuzzles(configurationCount, goalState)
    runId = 0
    if heuristic == "all":
        for key, heuristicFunc in domains.eightPuzzle.heuristics.items():
            configurationId = 0
            for configuration in configurations:
                problem = domains.eightPuzzle.puzzleProblem(configuration, goalState, heuristicFunc)
                path, stats = algorithm(problem)
                if path and stats:
                    printStats(runId, configurationId, stats, key)
                runId += 1
                configurationId += 1
    else:
        for configuration in configurations:
            problem = domains.eightPuzzle.puzzleProblem(configuration, goalState, domains.eightPuzzle.heuristics[heuristic])
            path, stats = algorithm(problem)
            if path and stats:
                printStats(runId, runId, stats, heuristic)
            runId += 1

    

if __name__ == "__main__":
    main()