


    # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
def dfs(self, s):
        visited = [False] * self.V
        self.dfs_util(s, visited)

def dfs_util(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    