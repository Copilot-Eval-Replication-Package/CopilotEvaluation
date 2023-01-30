# # # # # merge sort is a divide and conquer algorithm. it works by splitting the list into two parts and sorting them.
# # # # # the time complexity is O(n log n)
# # # # # the space complexity is O(n)
# # # # #
# # # # #
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


# # # # #
# # # # #
# # # # # # ! These were generate by CoPilot ALONGSIDE the function.
# # # # # def test_merge_sort():
# # # # #     print(""Testing merge sort"")
# # # # #     print(""Should be [1

