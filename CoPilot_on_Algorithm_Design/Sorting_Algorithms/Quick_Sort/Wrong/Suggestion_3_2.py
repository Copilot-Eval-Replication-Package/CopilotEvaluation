

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
    return left + right

print(sort_array([5, 3, 6, 2, 10]))