#Name: Haider Ali
#SAP ID: 70069779
from collections import deque # importing the deque class
from Graph import Graph #importing our graph class

def BFS(graph, start_vertex):
    visited = [False] * len(graph.graph) # creates a visited list that is false for every vertice
    queue = deque() # creates an empty queue
    queue.append(start_vertex) # appends the startvertex to the queue
    visited[start_vertex] = True

    while queue:
        v = queue.popleft() # if the queue is not empty, dequeue
        print(v, end=' ')

        for neighbour in graph.graph[v]:
            if not visited[neighbour]:
                queue.append(neighbour) # add all the adjacent (neighbouring nodes into the queue)
                visited[neighbour] = True
# time complexity O(V+E) where V is the number of vertices and E is the number of edges
# space complexity is O(V) due to both the queue and the visited array taking V space

# Example usage
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Breadth First Traversal (starting from vertex 2):")
BFS(g, 2)  # Passing the graph object and starting vertex to the BFS function