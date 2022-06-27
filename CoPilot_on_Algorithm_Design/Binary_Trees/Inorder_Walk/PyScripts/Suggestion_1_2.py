

        # if the node has a right child, call the function recusrsively on the right child and then print the value of the node and then call the function recursively on the left child.
    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.value)
        if self.right is not None:
            self.right.traverse()

    def traverse_recursive(self):
        print(self.value)
        if self.left is not None:
            self.left.traverse_recursive()
        if self.right is not None:
            self.right.traverse_recursive()

    def traverse_iterative(self):
        stack = []
        current = self
        while current is not None or len(stack) > 0:
            if current is not None:
                print(current.value)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

    def traverse_iterative_in_reverse(self):
        stack = []
        current = self
        while current is not None or len(stack) > 0:
            if current is not None:
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                print(current.value)
                current = current.left

    def traverse_in_order_traversal(self):
        if self.left is not None:
            self.left.traverse_in_order_traversal()
        print(self.value)
        if self.right is not None:
            self.right.traverse_in_order_traversal()

    def traverse_pre_order_traversal(self):
        print(self.value)
        if self.left is not None:
            self.left.traverse_pre_order_traversal()
        if self.right is not None:
            self.right.traverse_pre_order_traversal()

    def traverse_post_order_traversal(self

