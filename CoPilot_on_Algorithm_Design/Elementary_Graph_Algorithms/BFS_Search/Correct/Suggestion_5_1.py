


    # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
def dfs(self, s):
    visited = [False] * self.V
    stack = []
    stack.append(s)
    visited[s] = True
    while stack:
        s = stack.pop()
        print(s, end=" ")
        for i in self.graph[s]:
            if visited[i] == False:
                stack.append(i)
                visited[i] = True
    print()

    