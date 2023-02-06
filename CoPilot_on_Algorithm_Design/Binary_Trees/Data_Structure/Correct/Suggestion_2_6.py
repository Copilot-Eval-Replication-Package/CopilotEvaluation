

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                self.right.parent = self
            else:
                self.right.insert(value)
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self
    def delete(self, value):
        node = self.find(value)
        if node is None:
            return
        if node.left is None and node.right is None:
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is None:
            if node.parent.left is node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        elif node.right is None:
            if node.parent.left is node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.right.delete(successor.value)
    def preorder(self):
        if self is None:
            return
        print(self.value)
        