#
# ! This was generated by CoPilot ALONGSIDE the function.
def radix_sort(arr):
    # psuedo code:
    # for i in range(0, d):
    #     create a new array
    #     for j in range(0, n):
    #         if arr[j] % 10 ** i == 0:
    #             arr[j] = 0
    #         else:
    #             arr[j] = arr[j] % 10 ** i
    #     sort the new array
    #     for j in range(0, n):
    #         arr[j] = arr[j] + 10 ** i * new_array[j]
    # return arr

    d = len(str(max(arr)))
    for i in range(0, d):
        new_arr = [0] * len(arr)
        for j in range(0, len(arr)):
            if arr[j] % 10 ** i == 0:
                new_arr[j] = 0
            else:
                new_arr[j] = arr[j] % 10 ** i
        #new_arr = insertion_sort(new_arr)
        for j in range(0, len(arr)):
            arr[j] = arr[j] + 10 ** i * new_arr[j]
    return arr


#
#
# #
# #
# # # ! These were generate by CoPilot ALONGSIDE the function.
# # # def test_radix_sort():
# # #     print(""Testing radix sort"")
# # #     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
# # #     print(radix_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# # #
# # #

