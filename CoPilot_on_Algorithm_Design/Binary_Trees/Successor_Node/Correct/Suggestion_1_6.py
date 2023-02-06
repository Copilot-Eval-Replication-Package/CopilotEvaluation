


    
    # implement a function for finding the successor of a node in a tree. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node
def successor(self):
    if self.right is not None:
        return self.right.find_min_recursive()
    else:
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

   