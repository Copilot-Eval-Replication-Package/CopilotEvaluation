

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
        if self.dfs_cycle(s) == True:
            return False
        return True if self.dfs_cycle(d) == True else False

    # create a function that finds the shortest path between two vertices.
    def shortest_path(self, s, d):
        # ! what is the purpose of this function?
        self.visited = [False] * self.V
        self.parent = [None] * self.V
        self.parent[s] = -1
        self.dfs_util(s)
        self.visited = [False] * self.V
        self.parent = [None] * self.V
        self.parent[d] = -1
        self.dfs_util(d)
        self.visited = [False] * self.V
        self.parent = [None] * self.V
        self.parent[s] = -1
        self.dfs_util(s)
        self.visited = [False] * self.V
        self.parent = [None] * self.V
        self.parent[d] = -1
        self.dfs_util(d)
        self.visited = [False] * self.V
        self.parent = [None] * self.V
        self.parent[s] = -1
        self.dfs_util(s)
        self.visited = [False] * self.V
        self.parent = [None] * self.V
        self.parent[d] = -1
        self.dfs_util(d)
        print(""shortest path: "", end="""")
        self.print_path(d)
        print(""\n"")

    def print_path(self, d):
        if self.parent[d] == -1:
            print(d, end="" "")
            return
        self.print_path(self.parent[d])
        print(d, end="" "")

    # create a function that finds the shortest

