#generate test for above code

def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2]) == [1, 2]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([1, 3, 2]) == [1, 2, 3]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]