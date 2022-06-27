

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
    def minValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.minValue()

    # implement a function for finding the maximum value in a BST
    def maxValue(self):
        if self.right is None:
            return self.value
        else:
            return self.right.maxValue()

    # implement a function for finding the maximum value in a BST
    def get_successor(self):
        if self.right is not None:
            return self.right.minValue()
        else:
            return self.parent.get_successor()

    def get_predecessor(self):
        if self.left is not None:
            return self.left.maxValue()
        else:
            return self.parent.get_predecessor()

    def get_parent(self):
        if self.parent is None:
            return None
        else:
            return self.parent.value

    def get_left(self):
        if self.left is None:
            return None
        else:
            return self.left.value

    def get_right(self):
        if self.right is None:
            return None
        else:
            return self.right.value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return '{}'.format(self.value)"