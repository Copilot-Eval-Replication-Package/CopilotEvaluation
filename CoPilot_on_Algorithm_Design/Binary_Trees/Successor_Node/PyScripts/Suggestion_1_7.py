

def size(self):
        if self.left is None and self.right is None:
            pass
    
    # implement a function for finding the successor of a node in a tree. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
    def successor(self):
        if self.right is not None:
            return self.right.find_min_recursive()
        else:
            current = self
            while current.parent is not None and current.parent.right is current:
                current = current.parent
            return current.parent

    def successor_iterative(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the largest value in the tree that is less than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max_recursive()
        else:
            current = self
            while current.parent is not None and current.parent.left is current:
                current = current.parent
            return current.parent

    def predecessor_iterative(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    # implement a function for finding the sum of all the values in a tree
    def sum(self):
        if self.left is None and self.right is None:
            return self.value
        elif self.left is None:
            return self.value + self.right.sum()
        elif self.right is None:
            return self.value + self.left.sum()
        else:
            return self.value + self.left.sum() + self.right.sum()

    # implement a function for finding the sum of all the values in a tree
    def sum_iterative(self):
        current = self
        sum = 0
        while current is not None:
            sum += current.value
            current = current.left if current.left is not None else current.right
        return sum

    # implement a function for finding the sum of all the values in a tree
    def sum_recursive(self):
        if self.left is None and self.right is None:
            return self.value
        elif self.left

