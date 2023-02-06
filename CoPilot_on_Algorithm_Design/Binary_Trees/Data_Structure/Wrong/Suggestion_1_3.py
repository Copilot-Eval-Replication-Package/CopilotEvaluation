

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
                self.left.parent = self
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
                self.right.parent = self
        else:
            print("Value already in tree")
    def search(self, value):
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return None
        elif value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                return None
        else:
            return self
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            elif self.right is None:
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            elif self.left is None:
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
            else:
                predecessor = self.left.findMax()
                self.value

