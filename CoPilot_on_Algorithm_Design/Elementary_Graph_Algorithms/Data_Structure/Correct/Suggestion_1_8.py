

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def add_edge(self, v, w):
        self.graph[v][w] = 1
        self.graph[w][v] = 1

    def print_graph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.graph[i][j], end=' ')
            print()

    