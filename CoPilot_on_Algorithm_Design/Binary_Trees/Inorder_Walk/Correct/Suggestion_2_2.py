


    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    # if the node has a right child, call the function recusrsively on the right child and then print the value of the node and then call the function recursively on the left child.
def traverse(self):
    if self.left is not None:
        self.left.traverse()
    print(self.value)
    if self.right is not None:
        self.right.traverse()
   
