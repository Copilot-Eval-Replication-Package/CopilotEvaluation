

def dfs_cycle(self, s):
        self.visited[s] = True
        for i in self.graph[s]:
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return True
            elif self.visited[i] == True:
                return True
        return False

    # create a function that checks if two vetrices are reachable from each other. if they are the  function returns true otherwise false.
    def is_reachable(self, s, e):
        self.visited = [False] * self.V
        if self.dfs_cycle(s) == True:
            return False
        self.visited = [False] * self.V
        return True if self.dfs_cycle(e) == False else False

    def is_cyclic(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return True
        return False

    # create a function that checks if there is a path between two vertices. if there is a path, the function returns true otherwise false.
    def is_path(self, s, e):
        self.visited = [False] * self.V
        if self.dfs_cycle(s) == True:
            return False
        self.visited = [False] * self.V
        return True if self.dfs_cycle(e) == False else False

    # create a function that returns the number of connected components in a graph.
    def connected_components(self):
        self.visited = [False] * self.V
        count = 0
        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs(i)
                count += 1
        return count

    # create a function that returns the number of connected components in a graph.
    def is_connected(self, s, e):
        self.visited = [False] * self.V
        if self.dfs_cycle(s) == True:
            return False
        self.visited = [False] * self.V
        return True if self.dfs_cycle(e) == False else False

    # create a function that returns the number of connected components in a graph.
    def is_bridged(self, s, e):
        self.visited = [False] * self.V
        if self.dfs_cycle(s) ==

