

def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.value)
        if self.right is not None:
            self.right.traverse()

    # implement a function for finding the depth of a node in the tree. the depth of a node is the number of edges from the root to the node.
    def depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.depth()

    # implement a function for finding the depth of a node in the tree. the depth of a node is the number of edges from the root to the node.
    def depth_recursive(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.depth_recursive()

    # implement a function for finding the depth of a node in the tree. the depth of a node is the number of edges from the root to the node.
    def depth_iterative(self):
        current = self
        depth = 0
        while current.parent is not None:
            depth += 1
            current = current.parent
        return depth

    # implement a function for finding the height of a node in the tree. the height of a node is the number of edges from the node to the deepest leaf.
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # implement a function for finding the height of a node in the tree. the height of a node is the number of edges from the node to the deepest leaf.
    def height_recursive(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.height_recursive()
        elif self.right is None

