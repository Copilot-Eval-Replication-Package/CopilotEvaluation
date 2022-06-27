

def size(self):
        if self.left is None and self.right is None:
            pass
    
    # implement a function for finding the successor of a node in a tree. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
    def successor(self):
        if self.right is not None:
            return self.right.find_min_recursive()
        else:
            current = self
            while current.parent is not None and current is current.parent.right:
                current = current.parent
            return current.parent

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the largest value in the tree that is smaller than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max_recursive()
        else:
            current = self
            while current.parent is not None and current is current.parent.left:
                current = current.parent
            return current.parent

    # implement a function for finding the number of leaves in a tree
    def leaves(self):
        if self.left is None and self.right is None:
            return 1
        else:
            if self.left is None:
                return self.right.leaves()
            elif self.right is None:
                return self.left.leaves()
            else:
                return self.left.leaves() + self.right.leaves()

    # implement a function for finding the number of nodes in a tree
    def nodes(self):
        if self.left is None and self.right is None:
            return 1
        else:
            if self.left is None:
                return self.right.nodes()
            elif self.right is None:
                return self.left.nodes()
            else:
                return self.left.nodes() + self.right.nodes()

    # implement a function for finding the number of internal nodes in a tree
    def internal_nodes(self):
        if self.left is None and self.right is None:
            return 0
        else:
            if self.left is None:
                return self.right.internal_nodes()
            elif self.right is None:
                return self.left.internal_nodes()
            else:
                return self.left.internal

