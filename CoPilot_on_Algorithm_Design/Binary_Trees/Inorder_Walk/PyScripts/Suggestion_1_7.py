

def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    def level_order_traversal(self):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node to the farthest leaf node.
    def height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node to the farthest leaf node.
    def height_recursive(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.height_recursive()
        elif self.right is None:
            return 1 + self.left.height_recursive()
        else:
            return 1 + max(self.left.height_recursive(), self.right.height_recursive())

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node to the farthest leaf node.
    def height_iterative(self):
        current = self
        height = 0
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            height += 1
        return height

