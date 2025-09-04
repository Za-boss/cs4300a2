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
            8, 1, 2,
            3, 4, 5,
            6, 7, 0
        )
    )
    initialStateEasy = domains.eightPuzzle.puzzleState((
            1, 2, 5,
            3, 4, 8,
            0, 6, 7
    ))
    goalState = domains.eightPuzzle.puzzleState((
            0, 1, 2,
            3, 4, 5,
            6, 7, 8
        )   
    )
    #moves seem to be fine, but with state = initialState the loop seems to run for a very long time, I think there's something wrong with the algorithm itself
    #To try to solve this try the following
    #1. implement and use the misplaced heuristic and see if it fixes things
    #2. make sure costs are being computed correctly, there might be some problems with it and you should make sure it is being computed correctly
    #3. Make sure that the best_g map and frontier are working correctly, they may not be working correctly and you'll need to check it out
    #4. Try something else if you need to, ask the professor about it and see if he has anything to say, just throw things at the wall until somethin sticks
    problem = domains.eightPuzzle.puzzleProblem(initialStateEasy, goalState, heuristic)
    print(len(algorithm(problem)))

    

if __name__ == "__main__":
    main()