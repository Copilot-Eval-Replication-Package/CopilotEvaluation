def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            sorted_arr.append(right.pop(0))
        else:
            sorted_arr.append(left.pop(0))
    if len(left) > 0:
        sorted_arr.extend(left)
    if len(right) > 0:
        sorted_arr.extend(right)
    return sorted_arr
