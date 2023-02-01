

def selection_sort(arr):
    # psuedo code:
    # while unsorted list is not empty:
    #     find the smallest element in the unsorted list
    #     add it to the sorted list
    #     remove it from the unsorted list
    # return sorted list
    # ! it can't generate any more psuedo code.
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

