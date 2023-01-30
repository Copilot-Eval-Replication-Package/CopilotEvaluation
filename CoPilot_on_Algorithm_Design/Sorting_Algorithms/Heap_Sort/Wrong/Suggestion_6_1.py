

def heap_sort(arr):
    # create a max heap from the input array
    # heapify(arr)
    # for i in range(len(arr) - 1, -1, -1):
    #     arr[0], arr[i] = arr[i], arr[0]
    #     heapify(arr, 0, i)
    # return arr
    # create a max heap from the input array
    heapify(arr)
    # for i in range(len(arr) - 1, -1, -1):
    #     arr[0], arr[i] = arr[i], arr[0]
    #     heapify(arr, 0, i)
    # return arr
    # create a max heap from the input array
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

