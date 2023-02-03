



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

    