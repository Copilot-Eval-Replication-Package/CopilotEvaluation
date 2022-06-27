

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

    # implement a function for finding the minimum value in a BST
    def min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.min()

    # implement a function for finding the maximum value in a BST
    def max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.max()

    # implement a function for finding the successor of a BST node
    def successor(self):
        if self.right is not None:
            return self.right.min()
        else:
            p = self.parent
            while p is not None and p.right is self:
                self = p
                p = self.parent
            return p

    # implement a function for finding the predecessor of a BST node
    def predecessor(self):
        if self.left is not None:
            return self.left.max()
        else:
            p = self.parent
            while p is not None and p.left is self:
                self = p
                p = self.parent
            return p

    # implement a function for finding the size of a BST
    def size(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.size()
        elif self.right is None:
            return 1 + self.left.size()
        else:
            return 1 + self.left.size() + self.right.size()

    # implement a function for finding the height of a BST
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # implement a function for finding the depth of a BST node
    def depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.

