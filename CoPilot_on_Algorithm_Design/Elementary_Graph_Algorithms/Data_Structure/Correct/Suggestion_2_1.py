

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V           
        for i in range(self.V):
            self.graph[i] = []
# 
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
# 
    def is_connected(self, u, v):
        return True if v in self.graph[u] else False
# 
    def print_graph(self):
        for i in range(self.V):
            print(i, "-->", self.graph[i])
# 
