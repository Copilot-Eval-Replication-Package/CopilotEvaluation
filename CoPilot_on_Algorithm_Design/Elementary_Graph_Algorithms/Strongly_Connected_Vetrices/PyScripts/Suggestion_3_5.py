

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
    def is_reachable(self, s, d):
        self.visited = [False] * self.V
        if self.dfs(s) == True:
            if self.dfs(d) == True:
                return True
        return False

    # ! what is the purpose of this function?
    def is_cycle(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return True
        return False

    def bfs(self, s):
        queue = []
        queue.append(s)
        self.visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end="" "")
            for i in self.graph[s]:
                if self.visited[i] == False:
                    queue.append(i)
                    self.visited[i] = True

    def bfs_topological_sort(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                self.bfs(i)

    # ! what is the purpose of this function?
    def bfs_cycle(self, s):
        queue = []
        queue.append(s)
        self.visited[s] = True
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if self.visited[i] == False:
                    queue.append(i)
                    self.visited[i] = True
                elif self.visited[i] == True:
                    return True
        return False

    # create a function that checks if two vetrices are reachable from each other. if they are the  function returns true otherwise false.
    def is_reachable_bfs(self, s, d):
        self.visited = [False] * self.V
        if self

