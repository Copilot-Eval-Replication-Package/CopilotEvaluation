#generate test cases for above code

def test_bubble_sort():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    assert bubble_sort([1, 2]) == [1, 2]
    assert bubble_sort([2, 1]) == [1, 2]