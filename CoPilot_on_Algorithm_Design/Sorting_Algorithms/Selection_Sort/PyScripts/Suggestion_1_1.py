



def sort_array(arr):
    sorted_arr = []
    unsorted_arr = arr
    while len(unsorted_arr) > 0:
        smallest = unsorted_arr[0]
        for i in unsorted_arr:
            if i < smallest:
                smallest = i
        sorted_arr.append(smallest)
        unsorted_arr.remove(smallest)
    return sorted_arr

