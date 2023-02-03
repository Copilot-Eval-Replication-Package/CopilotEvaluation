

class Graph:
    def __init__(self):
        self.vertex_list = []
        self.adj_list = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            self.adj_list[vertex] = []
            self.num_vertices += 1

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.num_edges += 1

    def show(self):
        for key in self.adj_list:
            print(key, '->', self.adj_list[key])

    def depth_first_search(self, start):
        visited = []
        for vertex in self.adj_list:
            visited.append(False)
        self.depth_first_search_helper(start, visited)

    def depth_first_search_helper(self, start, visited):
        visited[start] = True
        print(start)
        for vertex in self.adj_list[start]:
            if visited[vertex] is False:
                self.depth_first_search_helper(vertex, visited)

    def breadth_first_search(self, start):
        visited = []
        for vertex in self.adj_list:
            visited.append(False)
        queue = []
        queue.append(start)
        visited[start] = True
        while len(queue) > 0:
            start = queue.pop(0)
            print(start)
            for vertex in self.adj_list[start]:
                if visited[vertex] is False:
                    queue.append(vertex)
                    visited[vertex] = True

    def topological_sort(self):
        visited = []
        for vertex in self.adj_list:
            visited.append(False)
        self.topological_sort_helper(

