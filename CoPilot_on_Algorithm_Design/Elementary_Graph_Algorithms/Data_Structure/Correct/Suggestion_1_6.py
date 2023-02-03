

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def print_graph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.graph[i][j], end=" ")
            print()
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    

