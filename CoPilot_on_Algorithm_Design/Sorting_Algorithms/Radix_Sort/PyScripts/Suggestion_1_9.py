def radix_sort(A):
    """"""
    # :param A: array of integers
    # :return: sorted array of integers
    """"""
    # get the maximum number of digits
    max_digits = 0
    for i in range(len(A)):
        if len(str(A[i])) > max_digits:
            max_digits = len(str(A[i]))
    # sort
    for i in range(max_digits):
        # create a new array
        B = []
        # for each digit, append to the new array
        for j in range(len(A)):
            B.append(A[j] % 10 ** (i + 1))
            A[j] = A[j] // 10 ** (i + 1)
        # sort the new array
        B.sort()
        # append the sorted array to the original array
        for j in range(len(B)):
            A[j] = A[j] * 10 ** (i + 1) + B[j]

    return A

