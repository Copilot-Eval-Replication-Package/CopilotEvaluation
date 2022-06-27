

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

    def bfs(self, s):
        visited = [False] * self.vertices
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for j in range(self.vertices):
                if self.graph[s][j] == 1 and visited[j] == False:
                    queue.append(j)
                    visited[j] = True

