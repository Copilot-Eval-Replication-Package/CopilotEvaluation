

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

    