def temp_sort(array):
    """"""
    # :param array: an array of integers, where each element has d digits, where the first digit is the lowest order digit, and the last digit is the highest order digit
    # :return: sorted array
    """"""
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

