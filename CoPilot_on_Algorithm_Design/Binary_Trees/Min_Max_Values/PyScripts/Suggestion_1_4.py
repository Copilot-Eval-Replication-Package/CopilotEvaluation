

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
    def find_min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_min()

    # implement a function for finding the maximum value in a BST
    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()

    # implement a function for finding the maximum value in a BST
    def find_successor(self):
        if self.right is None:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            return self.value
        else:
            return self.right.find_min()

    def find_predecessor(self):
        if self.left is None:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            return self.value
        else:
            return self.left.find_max()

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.value)
        if self.right is not None:
            self.right.print_tree()

    def print_tree_reverse(self):
        if self.right is not None:
            self.right.print_tree_reverse()
        print(self.value)
        if self.left is not None:
            self.left.print_tree_reverse()

    def __repr__(self):
        return str(self.value)

