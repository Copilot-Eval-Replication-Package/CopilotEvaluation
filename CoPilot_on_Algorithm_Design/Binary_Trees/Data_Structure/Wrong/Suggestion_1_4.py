

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
        node_to_delete = self.find(value)
        if node_to_delete is None:
            return False
        if node_to_delete.left is None or node_to_delete.right is None:
            if node_to_delete.left is None:
                child = node_to_delete.right
            else:
                child = node_to_delete.left
            if node_to_delete.parent is None:
                node_to_delete = child
            else:
                if node_to_delete is node_to_delete.parent.left:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
                if child is not None:
                    child.parent = node_to_delete.parent
            return True
        else:
            successor = node_to_delete.right
            while successor.left is not None:
                successor = successor.left
            node_to_delete.value = successor.value
            self.delete(successor.value)
  

