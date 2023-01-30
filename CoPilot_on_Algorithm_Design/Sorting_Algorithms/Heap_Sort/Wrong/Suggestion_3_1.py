#! Below comment was geenrated by copilot
# O(n) where n is the length of the input array
# O(n) where n is the length of the input array
def binary_tree_sort(array):
    tree = BinaryTree()
    for i in array:
        tree.insert(i)
    return tree.inorder()
