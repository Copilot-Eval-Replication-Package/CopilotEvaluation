

class BST:
    def __init__(self, v, p, l, r):
        self.vertex = v
        self.parent = p
        self.left = l
        self.right = r
        self.value = None

    def __str__(self):
        return str(self.vertex)

    def __repr__(self):
        return str(self.vertex)

