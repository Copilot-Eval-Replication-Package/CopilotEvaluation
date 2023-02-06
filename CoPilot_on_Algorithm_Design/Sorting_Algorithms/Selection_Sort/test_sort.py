#generate test cases for above code
def test_selection_sort():
    assert selection_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert selection_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
    assert selection_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert selection_sort([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]
    assert selection_sort([3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert selection_sort([1]) == [1]
    assert selection_sort([]) == []
    assert selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert selection_sort([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
