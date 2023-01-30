
# quick sort is a divide and conquer algorithm. it picks an element as pivot and partitions the array around the pivot such that all elements smaller than the pivot are to the left of it and all elements greater than the pivot are to the right of it.
# the time complexity is O(n log n)
# the space complexity is O(log n)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


