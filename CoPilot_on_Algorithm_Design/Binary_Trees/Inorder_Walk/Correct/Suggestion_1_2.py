

        # if the node has a right child, call the function recusrsively on the right child and then print the value of the node and then call the function recursively on the left child.
def traverse(self):
    if self.left is not None:
        self.left.traverse()
    print(self.value)
    if self.right is not None:
        self.right.traverse()

    
