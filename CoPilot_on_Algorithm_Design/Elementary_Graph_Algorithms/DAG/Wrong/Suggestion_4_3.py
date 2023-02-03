

class dag:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.visited = []
        self.stack = []
        self.topological_sort = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def topological_sort_helper(self, node):
        self.visited.append(node)
        for edge in self.edges:
            if edge[0] == node:
                if edge[1] not in self.visited:
                    self.topological_sort_helper(edge[1])
        self.stack.append(node)

    def topological_sort(self):
        for node in self.nodes:
            if node not in self.visited:
                self.topological_sort_helper(node)
        self.stack.reverse()
        return self.stack"