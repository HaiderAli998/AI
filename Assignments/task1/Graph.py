class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)] # using an adjacency list for this graph

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)