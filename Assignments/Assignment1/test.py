class PuzzleState:
    def __init__(self, puzzle, moves=0):
        self.puzzle = puzzle  # List of tile values
        self.moves = moves     # Total moves made so far
        self.parent = None     # Parent state for constructing the move sequence

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(tuple(self.puzzle))

    def __lt__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) < (other.moves + sum(other.puzzle))

    def __gt__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) > (other.moves + sum(other.puzzle))

    def __le__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) <= (other.moves + sum(other.puzzle))

    def __ge__(self, other):
        # Comparison based on total cost (moves + sum of tile values)
        return (self.moves + sum(self.puzzle)) >= (other.moves + sum(other.puzzle))

    def __str__(self):
        return f"PuzzleState(puzzle={self.puzzle}, moves={self.moves})"

def count_inversions(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions


# New solvable initial state
# New solvable initial state
solvable_initial_state = PuzzleState([1, 2, 3, 5, 8, 6, 4, 0, 7])

# New solvable goal state
solvable_goal_state = PuzzleState([1, 2, 3, 0, 5, 6, 4, 7, 8])



# Initial state inversions
initial_inversions = count_inversions(solvable_initial_state.puzzle)

# Goal state inversions
goal_inversions = count_inversions(solvable_goal_state.puzzle)

print("Initial state inversions:", initial_inversions)
print("Goal state inversions:", goal_inversions)

