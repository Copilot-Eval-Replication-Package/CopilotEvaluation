

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
    def is_reachable(self, s, v):
        self.visited = [False] * self.V
        if self.dfs(s) == True:
            return True
        return False

    # create a function that checks if two vetrices are reachable from each other. if they are the  function returns true otherwise false.
    def is_reachable_util(self, s, v):
        self.visited = [False] * self.V
        if self.dfs_util(s) == True:
            return True
        return False

    # create a function that checks if two vetrices are reachable from each other. if they are the  function returns true otherwise false.
    def is_reachable_topological_sort(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_util(i) == True:
                    return True
        return False

    # create a function that checks if two vetrices are reachable from each other. if they are the  function returns true otherwise false.
    def is_reachable_cycle(self, s, v):
        self.visited = [False] * self.V
        if self.dfs_cycle(s) == True:
            return True
        return False

