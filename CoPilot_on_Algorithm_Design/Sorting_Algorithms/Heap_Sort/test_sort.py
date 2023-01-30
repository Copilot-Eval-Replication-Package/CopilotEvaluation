def test_binary_tree_sort():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert heap_sort([1, 2, 2, 2, 2]) == [1, 2, 2, 2, 2]
    assert heap_sort([1]) == [1]
    assert heap_sort([]) == []
    assert heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert heap_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert heap_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



