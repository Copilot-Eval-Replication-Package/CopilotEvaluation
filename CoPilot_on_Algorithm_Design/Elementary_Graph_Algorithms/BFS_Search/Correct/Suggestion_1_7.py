


            
    # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
    # use BFS to solve this problem.
def BFS(self, s):
    queue = []
    visited = [False] * self.V
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True