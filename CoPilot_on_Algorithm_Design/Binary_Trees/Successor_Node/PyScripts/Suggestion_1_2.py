

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

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the largest value in the tree that is less than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            current = self
            while current.parent is not None and current.parent.left is current:
                current = current.parent
            return current.parent

    # implement a function for finding the number of leaves in a tree
    def num_leaves(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.num_leaves()
        elif self.right is None:
            return self.left.num_leaves()
        else:
            return self.left.num_leaves() + self.right.num_leaves()

    # implement a function for finding the number of nodes in a tree
    def num_nodes(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.num_nodes()
        elif self.right is None:
            return 1 + self.left.num_nodes()
        else:
            return 1 + self.left.num_nodes() + self.right.num_nodes()

    # implement a function for finding the number of internal nodes in a tree
    def num_internal_nodes(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.num_internal_nodes()
        elif self.right is None:
            return 1 +

