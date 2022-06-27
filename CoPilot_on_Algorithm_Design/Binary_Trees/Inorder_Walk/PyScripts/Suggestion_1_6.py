

def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    def traverse_tree(self):
        if self.left is not None:
            self.left.traverse_tree()
        print(self.value)
        if self.right is not None:
            self.right.traverse_tree()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    def traverse_tree_recursive(self):
        print(self.value)
        if self.left is not None:
            self.left.traverse_tree_recursive()
        if self.right is not None:
            self.right.traverse_tree_recursive()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    def traverse_tree_iterative(self):
        current = self
        while current is not None:
            print(current.value)
            if current.right is not None:
                current = current.right
            else:
                current = current.left

    # implement a function for printing the tree in order
    def print_in_order_traversal(self):
        if self.left is not None:
            self.left.print_in_order_traversal()
        print(self.value)
        if self.right is not None:
            self.right.print_in_order_traversal()

    # implement a function for printing the tree in order
    def print_in_order_traversal_recursive(self):
        print(self.value)
        if self.left is not None:
            self.left.print_in_order

