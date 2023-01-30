def heap_sort(arr):

    for i in range(len(arr)):
        heapify(arr, i)

    # one by one extract an element from heap
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i - 1)
    return arr
    # create a max heap from the input array
    for i in range(len(arr)):
        heapify(arr, i)

    # one by one extract an element from heap
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i - 1)
    return arr

    # create a max heap from the input array
    for i in range(len(arr)):
        heapify(arr, i)

    # one by one extract an element from heap
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i - 1)
    return arr

    # create a max heap from the input array
    for i in range(len(arr)):
        heapify(arr, i)

    # one by one extract an element from heap
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i - 1)
    return arr

