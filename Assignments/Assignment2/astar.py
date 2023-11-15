# Name : Haider Ali
# SAP ID : 70069779

import heapq
import random
import math

def heuristic_cost_estimate(current, goal):
    """
    Calculate the Manhattan distance heuristic between two points.

    Parameters:
    - current: Current node (x, y).
    - goal: Goal node (x, y).

    Returns:
    - Heuristic distance estimate.
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def simulated_annealing(current, neighbor, temperature):
    """
    Simulated Annealing acceptance probability function.

    Parameters:
    - current: Current node.
    - neighbor: Neighbor node.
    - temperature: Current temperature.

    Returns:
    - True if the move is accepted, False otherwise.
    """
    # Calculate the change in cost (heuristic distance)
    delta = heuristic_cost_estimate(current, neighbor)
    
    # If the new solution is better, accept it
    if delta < 0:
        return True

    # If the new solution is worse, accept it with a probability
    probability = math.exp(-delta / temperature)
    return random.uniform(0, 1) < probability

def hill_climbing(grid, current, goal):
    """
    Hill Climbing algorithm to explore neighboring nodes.

    Parameters:
    - grid: 2D grid representing the environment.
    - current: Current node (x, y).
    - goal: Goal node (x, y).

    Returns:
    - List of neighboring nodes.
    """
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for movement in movements:
        neighbor = (current[0] + movement[0], current[1] + movement[1])

        # Check if the neighbor is within the grid and is passable
        if (
            0 <= neighbor[0] < len(grid) and
            0 <= neighbor[1] < len(grid[0]) and
            grid[neighbor[0]][neighbor[1]] == 0
        ):
            neighbors.append(neighbor)

    return neighbors

def a_star_with_simulated_annealing(grid, start, goal, initial_temperature=1000, cooling_rate=0.99):
    """
    A* algorithm with Simulated Annealing.

    Parameters:
    - grid: 2D grid representing the environment.
    - start: Starting node (x, y).
    - goal: Goal node (x, y).
    - initial_temperature: Initial temperature for Simulated Annealing.
    - cooling_rate: Rate at which the temperature decreases.

    Returns:
    - Path from start to goal if a path is found, None otherwise.
    """
    open_set = [(0, start)]  # Priority queue to store nodes based on total cost
    closed_set = set()  # Set to keep track of visited nodes
    g_score = {start: 0}  # Dictionary to store the cost to reach each node
    f_score = {start: heuristic_cost_estimate(start, goal)}  # Dictionary to store total estimated cost for each node

    temperature = initial_temperature

    while open_set:
        current_f_score, current_node = heapq.heappop(open_set)

        if current_node == goal:
            # Reconstruct the path if the goal is reached
            path = []
            while current_node in g_score:
                path.append(current_node)
                current_node = g_score[current_node]
            return path[::-1]

        closed_set.add(current_node)

        neighbors = hill_climbing(grid, current_node, goal)

        for neighbor in neighbors:
            if neighbor not in closed_set:
                tentative_g_score = g_score[current_node] + 1

                # Use Simulated Annealing to decide whether to accept the move
                if simulated_annealing(current_node, neighbor, temperature):
                    if neighbor not in open_set or tentative_g_score < g_score.get(neighbor, 0):
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic_cost_estimate(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        temperature *= cooling_rate  # Decrease the temperature

    return None  # No path found

# Example usage:
grid_example = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

start_point = (0, 0)
goal_point = (4, 4)

path_result = a_star_with_simulated_annealing(grid_example, start_point, goal_point)
print("Path:", path_result)
