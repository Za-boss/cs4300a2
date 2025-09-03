import core
import argparse
def main():
    parser = argparse.ArgumentParser(description="Agent runner")
    parser.add_argument('--algo', type=str, required=False, default="AStar", choices=core.algorithms.keys())
    parser.add_argument('--configurationCount', '--cc', type=int, required=False, default=1)

    state = (
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
    )
    

if __name__ == "__main__":
    main()