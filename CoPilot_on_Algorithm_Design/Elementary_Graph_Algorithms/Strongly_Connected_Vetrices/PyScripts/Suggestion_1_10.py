

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
    def is_reachable(self, u, v):
        self.visited = [False] * self.V
        return self.dfs_cycle(u)

    def is_path(self, u, v):
        self.visited = [False] * self.V
        return self.dfs_cycle(u)

    # create a function that checks if the graph is a dag or not.
    def is_dag(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                if self.dfs_cycle(i) == True:
                    return False
        return True

    # create a function that returns the number of connected components in the graph.
    def count_connected_components(self):
        self.visited = [False] * self.V
        count = 0
        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs_util(i)
                count += 1
        return count

    def dfs_topological_sort_util(self, s):
        self.visited[s] = True
        for i in self.graph[s]:
            if self.visited[i] == False:
                self.dfs_topological_sort_util(i)
        print(s, end="" "")

    def dfs_topological_sort_util_2(self, s):
        self.visited[s] = True
        self.topological_sort.append(s)
        for i in self.graph[s]:
            if self.visited[i] == False:
                self.dfs_topological_sort_util_2(i)

    def dfs_topological_sort_util_3(self, s):
        self.visited[s] = True
        self.topological_sort.append(s)
        for i in self.graph[s]:
            if self.visited[i] == False:
                self.dfs_topological_sort"