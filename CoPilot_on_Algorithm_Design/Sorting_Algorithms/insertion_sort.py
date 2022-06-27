# create a function to sort an array of size n in ascending order:
# 1: Iterate from arr[0] to arr[n] over the array.
# 2: Compare the current element (key) to its predecessor.
# 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

import random


def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 56, 6]
    insertion_sort(test)
