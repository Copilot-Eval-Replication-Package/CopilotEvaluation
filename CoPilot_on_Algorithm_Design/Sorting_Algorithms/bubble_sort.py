# create a function that accepts a list of integers as input. the function repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

import random


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 56, 6]
    print(bubble_sort(test))
