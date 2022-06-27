

import random


def heap_sort(arr):
    # build a max heap
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)
    # extract the max element from the heap
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    return arr


def heapify(arr, i, n=None):
    if n is None:
        n = len(arr)
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)


if __name__ == ""__main__"":
    test = [random.randint(0, 100) for _ in range(10)]
    print(test)
    print(heap_sort(test))



