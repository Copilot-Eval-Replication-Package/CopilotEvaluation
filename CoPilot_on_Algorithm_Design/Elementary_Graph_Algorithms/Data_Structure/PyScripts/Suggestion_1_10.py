

class Graph:

    def __init__(self, graph):
        self.graph = graph

    def __len__(self):
        return len(self.graph)

    def __iter__(self):
        return iter(self.graph)

    def __getitem__(self, key):
        return self.graph[key]

    def __setitem__(self, key, value):
        self.graph[key] = value

    def __contains__(self, key):
        return key in self.graph

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return repr(self.graph)

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        self.graph[vertex1].remove(vertex2)
        self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        for i in self.graph[vertex]:
            self.graph[i].remove(vertex)
        del self.graph[vertex]

    def depth_first_search(self, start_vertex):
        visited = []
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(self.graph[vertex])
        return visited

    def breadth_first_search(self, start_vertex):
        visited = []
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(self.graph[vertex])
        return visited"