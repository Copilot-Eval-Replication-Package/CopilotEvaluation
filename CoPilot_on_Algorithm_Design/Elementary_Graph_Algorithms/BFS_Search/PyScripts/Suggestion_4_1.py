

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        for i in range(self.V):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self, u, v):
        return True if v in self.graph[u] else False

    def print_graph(self):
        for i in range(self.V):
            print(i, "-->", self.graph[i])
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
    def BFS(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

