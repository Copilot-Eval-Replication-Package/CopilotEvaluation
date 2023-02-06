



    # implement a function for finding the minimum value in a BST
def min(self):
    if self.left is None:
        return self.value
    else:
        return self.left.min()

    # implement a function for finding the maximum value in a BST
def max(self):
    if self.right is None:
        return self.value
    else:
        return self.right.max()

    

