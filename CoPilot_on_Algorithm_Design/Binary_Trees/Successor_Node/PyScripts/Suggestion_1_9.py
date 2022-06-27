

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

    # implement a function for finding the predecessor of a node in a tree. the predecessor of a node is the node that is the largest value in the tree that is less than the value of the node
    def predecessor(self):
        if self.left is not None:
            return self.left.find_max_recursive()
        else:
            current = self
            while current.parent is not None and current is current.parent.left:
                current = current.parent
            return current.parent

    # implement a function for finding the path from the root to a node in a tree. the path should be returned as a list of nodes from the root node down to the node
    def path_to(self, value):
        path = []
        current = self
        while current is not None:
            path.append(current)
            if current.value == value:
                break
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return path

    # implement a function for finding the lowest common ancestor of two nodes in a tree. the lowest common ancestor is the node that is an ancestor of both nodes and is the farthest from the two nodes
    def lca(self, node1, node2):
        if node1.value == node2.value:
            return node1
        elif node1.value < node2.value:
            return self.lca(node1.right, node2)
        else:
            return self.lca(node1.left, node2)

    # implement a function for finding the lowest common ancestor of two nodes in a tree. the lowest common ancestor is the node that is an ancestor of both nodes and is the farthest from the two nodes
    def lca_recursive(self, node1, node2):
        if node1.value == node2.value:

