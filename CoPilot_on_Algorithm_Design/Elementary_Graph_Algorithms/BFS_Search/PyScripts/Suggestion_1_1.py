

def print_graph(self):
        for i in range(self.V):
            print(i, ""-->"", self.graph[i])
            
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

