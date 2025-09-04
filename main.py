import core
import argparse
import domains.eightPuzzle
def main():
    parser = argparse.ArgumentParser(description="Agent runner")
    parser.add_argument('--algo', type=str, required=False, default="AStar", choices=core.algorithms.keys())
    parser.add_argument('--configurationCount', '--cc', type=int, required=False, default=1)
    parser.add_argument('--heuristic', '--h', type=str, required=False, default='null', choices=domains.eightPuzzle.heuristics.keys())
    args = parser.parse_args()
    algorithm = core.algorithms[args.algo]
    configurationCount = args.configurationCount
    heuristic = domains.eightPuzzle.heuristics[args.heuristic]
    
    # when you come back to this, make it so that the domain will generate a default configuration and get ready to start testing on that
    # random state generation will come after the program seems to be working
    initialState = domains.eightPuzzle.puzzleState((
            0, 3, 7,
            1, 8, 5,
            6, 2, 4
        )
    )
    goalState = domains.eightPuzzle.puzzleState((
            0, 1, 2,
            3, 4, 5,
            6, 7, 8
        )   
    )
    problem = domains.eightPuzzle.puzzleProblem(initialState, goalState, heuristic)
    print(algorithm(problem))

    

if __name__ == "__main__":
    main()