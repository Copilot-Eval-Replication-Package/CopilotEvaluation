# create a class that implements a directed acyclic graph data structure.
# ! faulty code same as others
class DAG:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        for i in range(self.V):
            self.graph[i] = []
        self.time = 0
        self.visited = [False] * self.V

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_connected(self, u, v):
        return True if v in self.graph[u] else False

    def print_graph(self):
        for i in range(self.V):
            print(i, "-->", self.graph[i])

    def dfs(self, s):
        self.visited[s] = True
        print(s, end=" ")
        for i in self.graph[s]:
            if self.visited[i] == False:
                self.dfs(i)

    def dfs_util(self, s):
        self.visited[s] = True
        print(s, end=" ")
        for i in self.graph[s]:
            if self.visited[i] == False:
                self.dfs_util(i)

    def dfs_topological_sort(self):
        self.visited = [False] * self.V
        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs_util(i)

    # ! what is the purpose of this function?
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
