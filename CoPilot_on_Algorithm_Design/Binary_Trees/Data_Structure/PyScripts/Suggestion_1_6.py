

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.vertices = []
        self.edges = []

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                self.left.parent = self
                self.vertices.append(value)
                self.edges.append((self.value, value))
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BST(value)
                self.right.parent = self
                self.vertices.append(value)
                self.edges.append((self.value, value))
            else:
                self.right.insert(value)
        else:
            self.vertices.append(value)
            self.edges.append((self.value, value))

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.search(value)
        else:
            return self

    def delete(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                self.left.delete(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                if self.parent.left == self:
                    self.parent.left = None
                elif self.parent.right == self:
                    self.parent.right = None
            elif self.left is None or self.right is None

