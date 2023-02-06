def inorder_traversal(self):
    if self.left is not None:
        self.left.inorder_traversal()
    print(self.value)
    if self.right is not None:
        self.right.inorder_traversal()

