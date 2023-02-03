

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def __str__(self):
        res = """"
        for v in self.vertices:
            res += str(v) + "": "" + str(self.vertices[v]) + ""\n""
        return res"