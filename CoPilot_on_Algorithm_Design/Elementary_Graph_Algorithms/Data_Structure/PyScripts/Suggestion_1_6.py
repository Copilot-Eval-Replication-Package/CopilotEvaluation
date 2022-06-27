

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def print_graph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.graph[i][j], end="" "")
            print()
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    def remove_edge(self, u, v):
        self.graph[u][v] = 0
        self.graph[v][u] = 0
    def is_connected(self, u, v):
        return self.graph[u][v] == 1
    def is_connected_bfs(self, u, v):
        queue = [u]
        visited = [False] * self.vertices
        visited[u] = True
        while queue:
            s = queue.pop(0)
            for i in range(self.vertices):
                if self.graph[s][i] == 1 and visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return visited[v]

