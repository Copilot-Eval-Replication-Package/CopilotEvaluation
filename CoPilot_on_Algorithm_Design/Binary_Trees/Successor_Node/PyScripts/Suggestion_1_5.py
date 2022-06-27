

def size(self):
        if self.left is None and self.right is None:
            pass
    
    # implement a function for finding the successor of a node in a tree. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
    def successor(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            current = self
            while current.parent is not None and current.parent.right is current:
                current = current.parent
            return current.parent

    def successor_iterative(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            current = self
            while current.parent is not None and current.parent.right is current:
                current = current.parent
            return current.parent

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the greatest value in the tree that is less than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            current = self
            while current.parent is not None and current.parent.left is current:
                current = current.parent
            return current.parent

    def predecessor_iterative(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            current = self
            while current.parent is not None and current.parent.left is current:
                current = current.parent
            return current.parent

    # implement a function for finding the number of leaves in a tree
    def leaves(self):
        if self.left is None and self.right is None:
            return 1
        else:
            return self.left.leaves() + self.right.leaves()

    def leaves_iterative(self):
        current = self
        leaves = 0
        while current is not None:
            if current.left is None and current.right is None:
                leaves += 1
            current = current.left if current.left is not None else current.right
        return leaves

    # implement a function for finding the number of internal nodes in a tree
    def internal_nodes(self):
        if self.left is None and self.right is None:
            return 0

