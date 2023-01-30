#
# # what is the time complexity of this algorithm?
# #! Below comment was geenrated by copilot
# O(n^2) where n is the length of the input array
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
