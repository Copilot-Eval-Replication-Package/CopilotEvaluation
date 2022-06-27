



#! Below comment was geenrated by copilot
# O(n) where n is the length of the input array
# O(n) where n is the length of the input array
def binary_tree_sort(array):
    tree = BinaryTree()
    for i in array:
        tree.insert(i)
    return tree.inorder()


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def inorder(self):
        if self.root is None:
            return []
        else:
            return self.root.inorder()

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.left is None and self.right is None:
            return [self.value]
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()


test = [random.randint(0, 100) for _ in range(10)]
print(test)
print(binary_tree_sort(test))







"