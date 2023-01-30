

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
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted_arr.append(left[0])
            left.remove(left[0])
        else:
            sorted_arr.append(right[0])
            right.remove(right[0])
    if len(left) > 0:
        sorted_arr.extend(left)
    else:
        sorted_arr.extend(right)
    return sorted_arr

print(sort_array([5, 3, 6, 2, 10]))