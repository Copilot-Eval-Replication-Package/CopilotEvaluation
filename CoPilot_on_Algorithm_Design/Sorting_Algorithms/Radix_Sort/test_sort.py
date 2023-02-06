# generate test case for above code
def generate_test_case():
    assert radix_sort([3, 1, 2]) == [1, 2, 3]
    assert radix_sort([1, 2, 3]) == [1, 2, 3]
    assert radix_sort([1, 1, 1]) == [1, 1, 1]
    assert radix_sort([1, 2]) == [1, 2]
    assert radix_sort([2, 1]) == [1, 2]
    assert radix_sort([1]) == [1]
    assert radix_sort([]) == []
    assert radix_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert radix_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert radix_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert radix_sort([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert radix_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]