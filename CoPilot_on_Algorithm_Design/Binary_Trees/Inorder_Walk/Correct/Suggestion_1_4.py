
def in_order_traversal(self):
    if self.left is not None:
        self.left.in_order_traversal()
    print(self.value)
    if self.right is not None:
        self.right.in_order_traversal()

    