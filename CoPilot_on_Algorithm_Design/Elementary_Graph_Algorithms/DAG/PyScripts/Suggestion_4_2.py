

class dag:
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
        self.stack.append(node)

    def topological_sort(self):
        for node in self.nodes:
            if node not in self.visited:
                self.dfs(node)
        while self.stack:
            self.topological_sort.append(self.stack.pop())
        return self.topological_sort

