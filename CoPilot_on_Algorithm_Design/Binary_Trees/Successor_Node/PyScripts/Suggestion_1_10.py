

def size(self):
        if self.left is None and self.right is None:
            pass
    
    # implement a function for finding the successor of a node in a tree. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
    def successor(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            parent = self.parent
            while parent is not None and parent.right is self:
                self = parent
                parent = self.parent
            return parent

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the largest value in the tree that is less than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            parent = self.parent
            while parent is not None and parent.left is self:
                self = parent
                parent = self.parent
            return parent

    # implement a function for finding the number of leaves in a tree
    def number_of_leaves(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.number_of_leaves()
        elif self.right is None:
            return self.left.number_of_leaves()
        else:
            return self.left.number_of_leaves() + self.right.number_of_leaves()

    # implement a function for finding the number of nodes in a tree
    def number_of_nodes(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.number_of_nodes()
        elif self.right is None:
            return 1 + self.left.number_of_nodes()
        else:
            return 1 + self.left.number_of_nodes() + self.right.number_of_nodes()

    # implement a function for finding the number of internal nodes in a tree
    def number_of_internal_nodes(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self."