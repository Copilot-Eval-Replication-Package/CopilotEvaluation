

class dag:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        # create a stack
        stack = []
        # create a visited array
        visited = [False] * self.vertices
        # create a topological order array
        topological_order = []
        # iterate through the vertices
        for i in range(self.vertices):
            # if the vertex is not visited
            if not visited[i]:
                # call the recursive function
                self.topological_sort_util(i, visited, stack, topological_order)
        # reverse the topological order array
        topological_order.reverse()
        # return the topological order array
        return topological_order

    def topological_sort_util(self, i, visited, stack, topological_order):
        # mark the vertex as visited
        visited[i] = True
        # iterate through the adjacent vertices
        for j in self.graph[i]:
            # if the adjacent vertex is not visited
            if not visited[j]:
                # call the recursive function
                self.topological_sort_util(j, visited, stack, topological_order)
        # push the vertex to the stack
        stack.append(i)

