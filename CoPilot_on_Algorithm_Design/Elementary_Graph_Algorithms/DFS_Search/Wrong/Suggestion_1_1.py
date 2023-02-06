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
    def bfs(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end="" "")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # the distnce between two vertxes is the smallest number of edges that need to be traversed to get from one vertex to reach the other.
    # create a fucntion that computes the distance between two vertxes and returns it.  if the vertxes are not reachable from each other, it should return 'not connected'.
    def bfs_distance(self, s, d):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        distance = [0] * self.V
        distance[s] = 0
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    distance[i] = distance[s] + 1
                    if i == d:
                        return distance[i]
        return "not connected"

    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
    def dfs(self, s):
        visited = [False] * self.V
        stack = []
        stack.append(s)
        visited[s] = True
        while stack:
            s = stack.pop()
            print(s, end="" "")
            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True

    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
    def dfs_recursive(self, s, visited):
        visited[s] = True
        print(s, end="" "")
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfs_recursive(i, visited)

