def selection_sort(arr):
    # psudeo code:
    # while unsorted list is not empty:
    #     find the smallest element in the unsorted list and append it to the sorted list.
    #     remove the smallest element from the unsorted list.
    # return the sorted list.
    sorted_list = []
    while len(arr) > 0:
        smallest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
        sorted_list.append(smallest)
        arr.remove(smallest)
    return sorted_list
