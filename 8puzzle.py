import heapq
from termcolor import colored

# Class to represent the state of the 8-puzzle
class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board  # The puzzle board configuration
        self.parent = parent  # Parent state
        self.move = move  # Move to reach this state
        self.depth = depth  # Depth in the search tree
        self.cost = cost  # Cost (depth + heuristic)

    def __lt__(self, other):
        return self.cost < other.cost

# Function to display the board in a visually appealing format
def print_board(board):
    print("+---+---+---+")
