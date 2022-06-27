

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

    def dfs_loop(self):
        for node in self.nodes:
            if node not in self.visited:
                self.dfs(node)

    def dfs_loop_stack(self):
        for node in self.nodes:
            if node not in self.visited:
                self.stack.append(node)
                self.visited.append(node)
                while self.stack:
                    for edge in self.edges:
                        if edge[0] == self.stack[-1] and edge[1] not in self.visited:
                            self.stack.append(edge[1])
                            self.visited.append(edge[1])
                            break
                    else:
                        self.topological_sort.append(self.stack.pop())

    def topological_sort_loop(self):
        self.dfs_loop_stack()
        self.topological_sort.reverse()

    def print_topological_sort(self):
        print(self.topological_sort)

