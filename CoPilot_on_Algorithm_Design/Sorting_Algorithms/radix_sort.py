# given an array of integers, where each element has d digits, where the first digit is the lowest order digit, and the last digit is the highest order digit,
# sort the array in ascending order by first comparing the lowest order digits and then higher order digits. the sorting should be done in linear time


# what is the time complexity of this algorithm?
#! Below comment was geenrated by copilot
# O(d(n+k)) where d is the number of digits in the largest number and k is the number of buckets
# O(n+k) where n is the length of the input array and k is the number of buckets
def radix_sort(array):
    max_digit = 0
    for i in array:
        if len(str(i)) > max_digit:
            max_digit = len(str(i))
    for i in range(1, max_digit + 1):
        buckets = [[] for _ in range(10)]
        for j in array:
            buckets[(j // 10 ** (i - 1)) % 10].append(j)
        array = []
        for k in buckets:
            array.extend(k)
    return array


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 56, 6]
    radix_sort(test)
