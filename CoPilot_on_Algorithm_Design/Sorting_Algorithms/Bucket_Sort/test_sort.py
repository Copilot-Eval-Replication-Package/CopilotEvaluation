
def test_bucket_sort():
    assert bucket_sort([0.1, 0.2, 0.3, 0.4, 0.5]) == [0.1, 0.2, 0.3, 0.4, 0.5]
    assert bucket_sort([0.5, 0.4, 0.3, 0.2, 0.1]) == [0.1, 0.2, 0.3, 0.4, 0.5]
    assert bucket_sort([0.5, 0.4, 0.3, 0.2, 0.1, 0.0]) == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    assert bucket_sort([0.1]) == [0.1]
    assert bucket_sort([]) == []
    assert bucket_sort([0.1, 0.2]) == [0.1, 0.2]
    assert bucket_sort([0.2, 0.1]) == [0.1, 0.2]