

def distance(self, u, v):
        if self.is_connected(u, v):
            visited = [False] * self.V
            queue = []
            queue.append(u)
            visited[u] = True
            while queue:
                u = queue.pop(0)
                for i in self.graph[u]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            visited = [False] * self.V
            queue = []
            queue.append(v)
            visited[v] = True
            while queue:
                v = queue.pop(0)
                for i in self.graph[v]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            return visited.count(True) - 1
        else:
            return 'not connected'
    # create a function that checks if two vetrices are reachable from each other. if they are the function returns true otherwise false.
    def is_reachable(self, u, v):
        if self.is_connected(u, v):
            visited = [False] * self.V
            queue = []
            queue.append(u)
            visited[u] = True
            while queue:
                u = queue.pop(0)
                for i in self.graph[u]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            visited = [False] * self.V
            queue = []
            queue.append(v)
            visited[v] = True
            while queue:
                v = queue.pop(0)
                for i in self.graph[v]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            return True if visited.count(True) - 1 == self.V - 1 else False
        else:
            return False
    # create a function that returns the number of connected components in the graph.
    def connected_components(self):
        visited = [False] * self.V
        count = 0
        for i in range(self.V):
            if visited[i] == False:
                queue = []
                queue.append(i)
                visited[i] = True
                while queue:
                    u = queue.pop(0)
                    for i in self.graph[u]:
                        if visited[i] == False:
                            queue.append(i)
                            visited[i] = True
                count += 1
        return count
    # create a function that returns the number of connected components in the graph.
    def is_bipartite(self):
        visited = [False] * self.V
        color = [-1] * self.V
        for i in range(self.V):
            if visited[i] == False:
                queue = []
                queue.append(i)
                visited[i] = True
                color[i] = 1
                while queue:
                    u = queue.pop(0)
                    for i in self.graph[u]:

