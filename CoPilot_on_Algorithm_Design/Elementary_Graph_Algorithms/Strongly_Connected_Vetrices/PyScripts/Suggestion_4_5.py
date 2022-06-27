

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
    # create a function that checks if a graph is bipartite or not.
    def is_bipartite(self):
        color = [None] * self.V
        for i in range(self.V):
            if color[i] == None:
                color[i] = 0
                queue = []
                queue.append(i)
                while queue:
                    u = queue.pop(0)
                    for i in self.graph[u]:
                        if color[i] == None:
                            color[i] = 1 - color[u]
                            queue.append(i)
                        elif color[i] == color[u]:
                            return False
        return True
    # create a function that checks if a graph is connected or not.
    def is_connected(self):
        visited = [False] * self.V
        queue = []
        queue.append(0)
        visited[0] = True
        while queue:
            u = queue.pop(0)
            for i in self.graph[u]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return

