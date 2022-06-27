

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
    # create a function that returns the list of all vertexes that can be reached from the source vertex.
    def reachable(self, s):
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
        print()
    # create a function that returns the list of all vertexes that can be reached from the source vertex.
    def reachable_from(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return visited.count(True) - 1
    # create a function that returns the list of all vertexes that"