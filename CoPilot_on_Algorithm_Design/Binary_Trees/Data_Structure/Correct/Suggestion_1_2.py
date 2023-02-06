

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
    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search(value)
        else:
            return True
    def delete(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                self.left.delete(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                if self.parent.left is self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            elif self.left is None:
                if self.parent.left is self:
                    self.parent.left = self.right
                    self.right.parent = self.parent
                else:
                    self.parent.right = self.right
                    self.right.parent = self.parent
            elif self.right is None:
                if self.parent.left is self:
                    self.parent.left = self.left
                    self.left.parent = self.parent
                else:
                    self.parent.right = self.left

