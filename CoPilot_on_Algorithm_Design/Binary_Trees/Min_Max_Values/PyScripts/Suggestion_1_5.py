

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

    # implement a function for finding the successor of a BST
    def find_successor(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            successor = self.parent
            while successor.right is self:
                self = successor
                successor = successor.parent
            return successor.value

    # implement a function for finding the predecessor of a BST
    def find_predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            predecessor = self.parent
            while predecessor.left is self:
                self = predecessor
                predecessor = predecessor.parent
            return predecessor.value

    # implement a function for finding the height of a BST
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return self.right.height() + 1
        elif self.right is None:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1

    # implement a function for finding the depth of a BST
    def depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.depth()

    # implement a function for finding the number of nodes in a BST
    def num_nodes(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.num_nodes()
        elif self.right is None:
            return 1 + self.left.num_nodes

