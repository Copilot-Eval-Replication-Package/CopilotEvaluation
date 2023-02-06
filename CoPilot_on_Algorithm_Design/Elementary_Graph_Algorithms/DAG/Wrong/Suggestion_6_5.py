

class Dag:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.visited = []
        self.stack = []
        self.topological_sort = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def dfs(self, node):
        self.visited.append(node)
        for edge in self.edges:
            if edge[0] == node and edge[1] not in self.visited:
                self.dfs(edge[1])

    def dfs_stack(self, node):
        self.visited.append(node)
        self.stack.append(node)
        for edge in self.edges:
            if edge[0] == node and edge[1] not in self.visited:
                self.dfs_stack(edge[1])
        self.topological_sort.append(self.stack.pop())

    def topological_sort_dfs(self):
        for node in self.nodes:
            if node not in self.visited:
                self.dfs(node)
        self.topological_sort = self.visited[::-1]

    def topological_sort_stack(self):
        for node in self.nodes:
            if node not in self.visited:
                self.dfs_stack(node)
        self.topological_sort = self.topological_sort[::-1]

    def print_topological_sort(self):
        print(self.topological_sort)"