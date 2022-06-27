

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def add_edge(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    def print_graph(self):
        for i in range(self.vertices):
            print(self.graph[i])

