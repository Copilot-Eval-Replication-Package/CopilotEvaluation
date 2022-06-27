

def sort_list(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort_list(arr[:mid])
    right = sort_list(arr[mid:])
    return merge(left, right)"