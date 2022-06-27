

def size(self):
        if self.left is None and self.right is None:
            pass
    
# implement a function for finding the successor of a node in a tree. the function recieves the value of a node as input. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node.
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

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node
    def is_balanced(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.right.height() <= 1
        elif self.right is None:
            return self.left.height() <= 1
        else:
            return abs(self.left.height() - self.right.height()) <= 1

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node
    def is_balanced_recursive(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.right.height() <= 1
        elif self.right is None:
            return self.left.height() <= 1
        else:
            return abs(self.left.height() - self.right.height()) <= 1

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node
    def is_balanced_iterative(self):

