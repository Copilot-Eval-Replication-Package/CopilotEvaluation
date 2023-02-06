



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

    