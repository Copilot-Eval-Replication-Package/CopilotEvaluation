

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        else:
            self.graph[from_vertex] = [to_vertex]

    def show_graph(self):
        for key in self.graph:
            print(key, self.graph[key])

 
