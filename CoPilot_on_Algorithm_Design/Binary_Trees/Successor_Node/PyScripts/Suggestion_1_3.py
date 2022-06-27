

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

    # implement a function for finding the inorder successor of a node in a tree. the inorder successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
    def in_order_successor(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            current = self
            while current.parent is not None and current.parent.right is current:
                current = current.parent
            return current.parent

    # implement a function for finding the inorder predecessor of a node in a tree. the inorder predecessor of a node is the node that is the largest value in the tree that is less than the value of the node
    def in_order_predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            current = self
            while current.parent is not None and current.parent.left is current:
                current = current.parent
            return current.parent

