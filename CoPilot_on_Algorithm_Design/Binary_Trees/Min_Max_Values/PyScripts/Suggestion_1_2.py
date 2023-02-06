

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
     

