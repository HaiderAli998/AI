from queue import Queue, LifoQueue, PriorityQueue

class PuzzleState:
    def __init__(self, puzzle, moves=0, parent=None):
        self.puzzle = puzzle
        self.moves = moves
        self.parent = parent

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return (self.moves + sum(self.puzzle)) < (other.moves + sum(other.puzzle))
    def __str__(self):
        return f"PuzzleState(puzzle={self.puzzle}, moves={self.moves})"

    def __hash__(self):
        return hash(tuple(self.puzzle))


    def __gt__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) > (other.moves + sum(other.puzzle))

    def __le__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) <= (other.moves + sum(other.puzzle))

    def __ge__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) >= (other.moves + sum(other.puzzle))



def is_valid_move(position):
    """Check if a move is valid within the puzzle grid."""
    return 0 <= position < 9

def get_adjacent_states(state):
    """Generate adjacent states by moving the empty tile."""
    moves = [1, -1, 3, -3]  # Right, Left, Down, Up
    empty_tile_index = state.puzzle.index(0)
    adjacent_states = []

    for move in moves:
        new_position = empty_tile_index + move

        if is_valid_move(new_position):
            new_puzzle = state.puzzle[:]
            new_puzzle[empty_tile_index], new_puzzle[new_position] = new_puzzle[new_position], new_puzzle[empty_tile_index]
            adjacent_states.append(PuzzleState(new_puzzle, state.moves + new_puzzle[new_position]))
            # Set the parent state for constructing the move sequence
            adjacent_states[-1].parent = state

    return adjacent_states

def count_inversions(puzzle):
    """Count the number of inversions in the puzzle state."""
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions

def is_solvable(state):
    """Check if the given puzzle state is solvable."""
    inversions = count_inversions(state.puzzle)
    blank_tile_row = state.puzzle.index(0) // 3  # Row index of the blank tile from the bottom
    return (inversions % 2 == 0 and blank_tile_row % 2 == 1) or \
           (inversions % 2 == 1 and blank_tile_row % 2 == 0)

def breadth_first_search(initial_state, goal_state):
    """Perform Breadth-First Search on the 8-puzzle."""
    frontier = Queue()
    explored = set()

    frontier.put(initial_state)
    explored.add(tuple(initial_state.puzzle))

    while not frontier.empty():
        current_state = frontier.get()

        if current_state == goal_state:
            return current_state.moves, extract_move_sequence(current_state)

        for neighbor in get_adjacent_states(current_state):
            if tuple(neighbor.puzzle) not in explored:
                # Set the parent for constructing the move sequence
                neighbor.parent = current_state
                frontier.put(neighbor)
                explored.add(tuple(neighbor.puzzle))

    return -1, []  # No solution found
# Depth-First Search
def depth_first_search(initial_state, goal_state):
    """Perform Depth-First Search on the 8-puzzle."""
    frontier = []
    explored = set()

    frontier.append(initial_state)
    explored.add(tuple(initial_state.puzzle))

    while frontier:
        current_state = frontier.pop()

        if current_state == goal_state:
            return current_state.moves, extract_move_sequence(current_state)

        for neighbor in get_adjacent_states(current_state):
            if tuple(neighbor.puzzle) not in explored:
                # Set the parent for constructing the move sequence
                neighbor.parent = current_state
                frontier.append(neighbor)
                explored.add(tuple(neighbor.puzzle))

    return -1, []  # No solution found

def iterative_deepening(initial_state, goal_state):
    """Perform Iterative Deepening Search with a maximum depth of 2 on the 8-puzzle."""
    max_depth = 11

    for depth in range(max_depth + 1):
        result, move_sequence = depth_limited_search(initial_state, goal_state, depth)

        if result != -1:
            return result, move_sequence

    return -1, []  # No solution found within the maximum depth


def depth_limited_search(current_state, goal_state, depth):
    """Perform Depth-Limited Search with a specified depth limit."""
    if depth == 0 and current_state == goal_state:
        return current_state.moves, [current_state]

    if depth > 0:
        for neighbor in get_adjacent_states(current_state):
            result, move_sequence = depth_limited_search(neighbor, goal_state, depth - 1)
            if result != -1:
                move_sequence.insert(0, current_state)  # Insert current state at the beginning
                return result, move_sequence

    return -1, []  # No solution found within the given depth

def uniform_cost_search(initial_state, goal_state):
    """Perform Uniform Cost Search on the 8-puzzle."""
    frontier = PriorityQueue()
    explored = set()
    frontier.put((initial_state.moves, initial_state))

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == goal_state:
            move_sequence = extract_move_sequence(current_state)
            return current_state.moves, move_sequence

        for neighbor in get_adjacent_states(current_state):
            if neighbor not in explored:
                # Set the parent for constructing the move sequence
                neighbor.parent = current_state
                frontier.put((neighbor.moves, neighbor))
                explored.add(neighbor)

    return -1, []  # No solution found

def extract_move_sequence(state):
    """Extract the move sequence from the goal state to the initial state."""
    move_sequence = []
    while state:
        move_sequence.insert(0, state)
        state = state.parent
    return move_sequence

# Example usage
if __name__ == "__main__":
    # Initialize the initial and goal states
    # Solvable initial state
    initial = PuzzleState([1, 2, 3, 5, 8, 6, 4, 0, 7])
    # Solvable goal state
    goal = PuzzleState([1, 2, 3, 0, 5, 6, 4, 7, 8])
    # Check if initial and goal states are solvable
    if not is_solvable(initial):
        print("Initial state is not solvable.")
    elif not is_solvable(goal):
        print("Goal state is not solvable.")
    else:
        # Perform Breadth-First Search
        bfs_moves, bfs_move_sequence = breadth_first_search(initial, goal)
        print("Breadth-First Search:", "Solution found" if bfs_moves != -1 else "No solution")
        if bfs_moves != -1:
            print("Move sequence:")
            for state in bfs_move_sequence:
                print(state.puzzle)

        # Perform Depth-First Search
        dfs_moves, dfs_move_sequence = depth_first_search(initial, goal)
        print("Depth-First Search:", "Solution found" if dfs_moves != -1 else "No solution")
        if dfs_moves != -1:
            print("Move sequence:")
            for state in dfs_move_sequence:
                print(state.puzzle)

        # Perform Iterative Deepening Search
        id_moves, id_move_sequence = iterative_deepening(initial, goal)
        print("Iterative Deepening:", "Solution found" if id_moves != -1 else "No solution")
        if id_moves != -1:
            print("Move sequence:")
            for state in id_move_sequence:
                print(state.puzzle)

        # Perform Uniform Cost Search
        ucs_moves, ucs_move_sequence = uniform_cost_search(initial, goal)
        print("Uniform Cost Search:", "Solution found" if ucs_moves != -1 else "No solution")
        if ucs_moves != -1:
            print("Move sequence:")
            for state in ucs_move_sequence:
                print(state.puzzle)
