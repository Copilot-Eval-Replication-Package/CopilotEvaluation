#
# ! This was generated by CoPilot ALONGSIDE the function.
def radix_sort(arr):

    for i in range(0, d):

        for j in range(0, n):
            if arr[j] % 10 ** i == 0:
                arr[j] = 0
            else:
                arr[j] = arr[j] % 10 ** i

        for j in range(0, n):
            if arr[j] == 0:
                arr[j] = 0
            else:
                arr[j] = arr[j] / 10 ** i
    return arr


# #
# #
# # #
# # #
# # # # ! These were generate by CoPilot ALONGSIDE the function.
# # # # def test_radix_sort():
# # # #     print(""Testing radix sort"")
# # # #     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
# # # #     print(radix_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# # # #     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
# # # #     print(radix_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# # # #     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
# # # #     print(radix_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# # # #     print(""Should be [1, 2, 3, 4

