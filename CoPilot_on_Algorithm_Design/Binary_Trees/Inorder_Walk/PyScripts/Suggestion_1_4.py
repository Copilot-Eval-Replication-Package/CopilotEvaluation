

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
    def traversal(self):
        if self.left is not None:
            self.left.traversal()
        print(self.value)
        if self.right is not None:
            self.right.traversal()

    def traversal_recursive(self):
        if self.left is not None:
            self.left.traversal_recursive()
        print(self.value)
        if self.right is not None:
            self.right.traversal_recursive()

    def traversal_iterative(self):
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            print(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

