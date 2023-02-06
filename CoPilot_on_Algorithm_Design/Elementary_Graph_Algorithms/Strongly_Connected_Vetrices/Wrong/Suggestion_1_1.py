


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
        else:
            return True
    # create a function that checks if the graph is a dag. if it is a dag it returns true otherwise false.
    def is_dag(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return False
        return True

    # create a function that checks if the graph is a DAG. if it is a DAG it returns true otherwise false.
    def is_dag_util(self, s):
        self.visited[s] = True
        for i in self.graph[s]:
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return False
        return True

    def dfs_topological_sort_util(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return False
        return True

    def dfs_topological_sort(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return False
        return True

    # create a function that checks if the graph is a DAG. if it is a DAG it returns true otherwise false.
    def is_dag(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return False
        return


