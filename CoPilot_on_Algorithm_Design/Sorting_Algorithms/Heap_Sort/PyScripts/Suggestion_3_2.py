



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
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def inorder(self):
        values = []
        self._inorder(self.root, values)
        return values

    def _inorder(self, node, values):
        if node is not None:
            self._inorder(node.left, values)
            values.append(node.value)
            self._inorder(node.right, values)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == ""__main__"":
    test = [random.randint(0, 100) for _ in range(10)]
    print(test)
    print(binary_tree_sort(test))



