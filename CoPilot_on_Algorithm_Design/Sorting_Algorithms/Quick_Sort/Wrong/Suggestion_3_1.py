

def sort_array(arr):
    left = []
    right = []
    for i in range(len(arr)):
        if i % 2 == 0:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left.sort()
    right.sort()
    sorted_arr = []
    for i in range(len(left)):
        sorted_arr.append(left[i])
        sorted_arr.append(right[i])
    return sorted_arr

print(sort_array([5, 3, 6, 2, 10]))

