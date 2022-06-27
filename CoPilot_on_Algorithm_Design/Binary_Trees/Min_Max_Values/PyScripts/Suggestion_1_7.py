

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
    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()

    # implement a function for finding the maximum value in a BST
    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()

    # implement a function for finding the maximum value in a BST
    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()

    def inorder_print(self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.value)
        if self.right is not None:
            self.right.inorder_print()

    def preorder_print(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder_print()
        if self.right is not None:
            self.right.preorder_print()

    def postorder_print(self):
        if self.left is not None:
            self.left.postorder_print()
        if self.right is not None:
            self.right.postorder_print()
        print(self.value)

    def breadth_first_search(self):
        queue = [self]
        while queue:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)

