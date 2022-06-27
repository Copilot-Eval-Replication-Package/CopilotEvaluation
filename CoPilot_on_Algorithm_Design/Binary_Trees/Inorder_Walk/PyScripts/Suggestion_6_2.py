

def traverse(self):
    if self.left is None and self.right is None:
        print(self.value)
    elif self.left is None:
        print(self.value)
        self.right.traverse()
    elif self.right is None:
        self.left.traverse()
        print(self.value)
    else:
        self.left.traverse()
        print(self.value)
        self.right.traverse()
    # implement a function for finding the maximum value in a BST
    def find_max(self):
        if self.right is None:
            return self
        else:
            return self.right.find_max()
    # implement a function for finding the successor of a node in a BST
    def find_successor(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            temp = self
            while temp.parent is not None and temp.parent.right is temp:
                temp = temp.parent
            return temp.parent
    # implement a function for finding the predecessor of a node in a BST
    def find_predecessor(self):
        if self.left is not None:
            return self.left.find_max()
        else:
            temp = self
            while temp.parent is not None and temp.parent.left is temp:
                temp = temp.parent
            return temp.parent
    # implement a function for finding the height of a BST
    def find_height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.find_height()
        elif self.right is None:
            return 1 + self.left.find_height()
        else:
            return 1 + max(self.left.find_height(), self.right.find_height())
    # implement a function for finding the depth of a node in a BST
    def find_depth(self):
        temp = self
        depth = 0
        while temp.parent is not None:
            temp =

