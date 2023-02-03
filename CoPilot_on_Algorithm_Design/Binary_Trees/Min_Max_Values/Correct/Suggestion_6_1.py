


    # implement a function for finding the minimum value in a BST
def findMin(self):
    if self.left is None:
        return self
    else:
        return self.left.findMin()
    # implement a function for finding the maximum value in a BST
def findMax(self):
    if self.right is None:
        return self
    else:
        return self.right.findMax()
    