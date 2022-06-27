

def size(self):
        if self.left is None and self.right is None:
            pass
    
    # implement a function for finding the successor of a node in a tree. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
    def successor(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            current = self
            while current.parent is not None:
                if current.parent.left is current:
                    return current.parent
                current = current.parent
        return None

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the largest value in the tree that is less than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            current = self
            while current.parent is not None:
                if current.parent.right is current:
                    return current.parent
                current = current.parent
        return None

    # implement a function for finding the number of leaves in a BST
    def number_of_leaves(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.number_of_leaves()
        elif self.right is None:
            return self.left.number_of_leaves()
        else:
            return self.left.number_of_leaves() + self.right.number_of_leaves()

    def number_of_leaves_iterative(self):
        current = self
        leaves = 0
        while current is not None:
            if current.left is None and current.right is None:
                leaves += 1
            current = current.left if current.left is not None else current.right
        return leaves

    # implement a function for finding the number of internal nodes in a BST
    def number_of_internals(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.number_of_internals()
        elif self.right is None:
            return 1 + self.left.number_of_internals()
        else:
            return 1 + self

