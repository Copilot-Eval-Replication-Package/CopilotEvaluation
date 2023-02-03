

    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
def dfs_recursive(self, s, visited):
    visited[s] = True
    print(s, end=" ")
    for i in self.graph[s]:
        if visited[i] == False:
            self.dfs_recursive(i, visited)

# given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
def dfs_recursive_all(self, s):
    visited = [False] * self.V
    for i in range(self.V):
        if visited[i] == False:
            self.dfs_recursive(i, visited)

    