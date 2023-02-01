def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        min_value = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_value:
                min_index = j
                min_value = arr[j]
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

