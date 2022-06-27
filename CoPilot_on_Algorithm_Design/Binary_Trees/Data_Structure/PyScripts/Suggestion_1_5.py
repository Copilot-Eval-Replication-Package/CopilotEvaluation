

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def insert(self,value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
                self.right.parent = self
    def find(self,value):
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value > self.value and self.right:
            return self.right.find(value)
        else:
            return None
    def delete(self,value):
        node = self.find(value)
        if node is None:
            return None
        elif node.left and node.right:
            min_node = node.right.find_min()
            node.value = min_node.value
            node.right.delete(min_node.value)
        elif node.left or node.right:
            if node.left:
                child = node.left
            else:
                child = node.right
            child.parent = node.parent
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self = child
        else:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self = None
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self
    def find_max(self):
        if self

