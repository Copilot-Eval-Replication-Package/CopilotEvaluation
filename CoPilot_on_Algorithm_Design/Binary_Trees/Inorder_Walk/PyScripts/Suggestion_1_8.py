

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                self.right.parent = self
            else:
                self.right.insert(value)

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search(value)
        else:
            return True

    def delete(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                self.left.delete(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                if self.parent.left is self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            elif self.left is None:
                if self.parent.left is self:
                    self.parent.left = self.right
                    self.right.parent = self.parent
                else:
                    self.parent.right = self.right
                    self.right.parent = self.parent
            elif self.right is None:
                if self.parent.left is self:
                    self.parent.left = self.left
                    self.left.parent = self.parent
                else:
                    self.parent.right = self.left

    # implement a function for finding the minimum value in a BST
    def find_min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_min()

    # implement a function for finding the maximum value in a BST
    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()

    # implement a function for finding the maximum value in a BST
    def find_max_recursive(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max_recursive()

    # implement a function for finding the minimum value in a BST
    def find_min_recursive(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_min_recursive()

    # implement a function for finding the minimum value in a BST
    def find_min_iterative(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    # implement a function for finding the minimum value in a BST
    def find_max_iterative(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.value)
        if self.right is not None:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_traversal()
        if self.right is not None:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    # if the node has a right child, call the function recusrsively on the right child and then print the value of the node and then call the function recursively on the left child.

    def tree_height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.tree_height()
        elif self.right is None:
            return 1 + self.left.tree_height()
        else:
            return 1 + max(self.left.tree_height(), self.right.tree_height())

    def tree_height_recursive(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.tree_height_recursive()
        elif self.right is None:
            return 1 + self.left.tree_height_recursive()
        else:
            return 1 + max(self.left.tree_height_recursive(), self.right.tree_height_recursive())

    def tree_height_iterative(self):
        current = self
        height = 0
        while current is not None:
            if current.left is None and current.right is None:
                return height
            elif current.left is None:
                current = current.right
            elif current.right is None:
                current = current.left
            else:
                current = current.left
            height += 1
        return height

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.value)
        if self.right is not None:
            self.right.print_tree()

    de"