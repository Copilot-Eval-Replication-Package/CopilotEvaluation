def selection_sort(arr):
    sorted_array = []
    while len(arr) > 0:
        max_index = 0
        for i in range(len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        sorted_array.append(arr.pop(max_index))
    return sorted_array

