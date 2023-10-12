#Name: Haider Ali
#SAP ID: 70069779
from Graph import Graph
def DFS(graph,start_vertex=0):
    stack = [start_vertex] # creates an empty stack and pushes the start vertex
    visited = [False] * graph.V # creates visited and sets it to empty

    while stack: # if there are still vertices on the stack
        v = stack.pop() # pop the vertice
        if not visited[v]:
            visited[v] = True #set the vertice to true
            print(v, end=' ')
            # Push unvisited neighbors onto the stack
            for neighbour in reversed(graph.graph[v]):
                if not visited[neighbour]:
                    stack.append(neighbour)
# time complexity O(V+E) where V is the number of vertices and E is the number of edges
# space complexity is O(V) due to both the stack and the visited array taking V space
# Creating a graph with 4 vertices
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Depth First Traversal (starting from vertex 2):")
DFS(g,2)  # Passing the graph object to the standalone DFS function