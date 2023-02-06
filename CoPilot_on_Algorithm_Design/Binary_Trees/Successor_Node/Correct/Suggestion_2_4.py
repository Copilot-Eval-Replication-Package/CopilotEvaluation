



    # implement a function for finding the successor of a node in a tree. the function recieves the value of a node as input. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node.
def successor(self, value):
    if self.value == value:
        if self.right is not None:
            return self.right.find_min()
        else:
            return None
    elif value < self.value:
        if self.left is not None:
            return self.left.successor(value)
        else:
            return None
    else:
        if self.right is not None:
            return self.right.successor(value)
        else:
            return None

    