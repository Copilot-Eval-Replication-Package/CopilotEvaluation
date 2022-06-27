

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                self.right.parent = self
            else:
                self.right.insert(value)

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search(value)
        else:
            return True

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

    # implement a function for finding the maximum value in a BST
    def find_max_recursive(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max_recursive()

    # implement a function for finding the minimum value in a BST
    def find_min_recursive(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_min_recursive()

    # implement a function for finding the minimum value in a BST
    def find_min_iterative(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    # implement a function for finding the minimum value in a BST
    def find_max_iterative(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.value)
        if self.right is not None:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_traversal()
        if self.right is not None:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()

    # implement a function for travesing the tree. the function should the value of the node, find the node. if the node has no children, print the value of the node.
    # if the node has a left child, call the function recusrsively on the left child and then print the value of the node and then call the function recursively on the right child.
    # if the node has a right child, call the function recusrsively on the right child and then print the value of the node and then call the function recursively on the left child.
    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.value)
        if self.right is not None:
            self.right.traverse()

    def traverse_recursive(self):
        print(self.value)
        if self.left is not None:
            self.left.traverse_recursive()
        if self.right is not None:
            self.right.traverse_recursive()

    # implement a function for finding the height of a tree. the height of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def height_iterative(self):
        current = self
        height = 0
        while current is not None:
            height += 1
            current = current.left if current.left is not None else current.right
        return height

    # implement a function for finding the depth of a node in a tree. the depth of a node is the number of edges along the path from the root node down to the node
    def depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.depth()

    def depth_iterative(self):
        current = self
        depth = 0
        while current.parent is not None:
            current = current.parent
            depth += 1
        return depth

    # implement a function for finding the number of nodes in a tree
    def size(self):
        if self.left is None and self.right is None:
            pass

    # implement a function for finding the successor of a node in a tree. the function recieves the value of a node as input. the successor of a node is the node that is the smallest value in the tree that is greater than the value of the node.
    def successor(self, value):
        if self.value == value:
            if self.right is not None:
                return self.right.find_min()
            else:
                return None
        elif value < self.value:
            if self.left is not None:
                return self.left.successor(value)
            else:
                return None
        else:
            if self.right is not None:
                return self.right.successor(value)
            else:
                return None

    # implement a function for finding the predecessor of a node in a tree. the function recieves the value of a node as input. the predecessor of a node is the node that is the largest value in the tree that is less than the value of the node.
    def predecessor(self, value):
        if self.value == value:
            if self.left is not None:
                return self.left.find_max()
            else:
                return None
        elif value < self.value:
            if self.left is not None:
                return self.left.predecessor(value)
            else:
                return None
        else:
            if self.right is not None:
                return self.right.predecessor(value)
            else:
                return None

    # implement a function for finding the number of leaves in a tree
    def number_of_leaves(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.number_of_leaves()
        elif self.right is None:
            return self.left.number_of_leaves()
        else:
            return self.left.number_of_leaves() + self.right.number_of_leaves()

    # implement a function for finding the number of internal nodes in a tree
    def number_of_internal_nodes(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.number_of_internal_nodes

