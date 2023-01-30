# # # # # merge sort is a divide and conquer algorithm. it works by splitting the list into two parts and sorting them.
# # # # # the time complexity is O(n log n)
# # # # # the space complexity is O(n)
# # # # #
# # # # #
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


# # # # #
# # # # #
# # # # # # ! These were generate by CoPilot ALONGSIDE the function.
# # # # # def test_merge_sort():
# # # # #     print(""Testing merge sort"")
# # # # #     print(""Should be [1

