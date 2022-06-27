

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def show(self):
        print(self.graph)

    def show_edges(self):
        for key in self.graph.keys():
            print(key, end=' -> ')
            for value in self.graph[key]:
                print(value, end=' ')
            print()

    def show_vertices(self):
        print(self.graph.keys())

    def has_vertex(self, vertex):
        if vertex in self.graph.keys():
            return True
        else:
            return False

    def has_edge(self, vertex1, vertex2):
        if vertex1 in self.graph.keys() and vertex2 in self.graph.keys():
            if vertex2 in self.graph[vertex1]:
                return True
            else:
                return False
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph.keys() and vertex2 in self.graph.keys():
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)
        else:
            return False

    def remove_vertex(self, vertex):
        if vertex in self.graph.keys():
            for value in self.graph[vertex]:
                self.graph[value].remove(vertex)
            self.graph.pop(vertex)
        else:
            return False

    def dfs(self, start, end):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited

