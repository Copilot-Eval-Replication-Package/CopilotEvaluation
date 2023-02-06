

class DAG:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        for i in range(self.V):
            self.graph[i] = []
        self.time = 0
        self.visited = [False] * self.V

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_connected(self, u, v):
        return True if v in self.graph[u] else False

    def print_graph(self):
        for i in range(self.V):
            print(i, "-->", self.graph[i])

    