#generate test case for the function
def test_check_overlap():
    assert check_overlap((1, 2), (3, 4)) == True
    assert check_overlap((3, 4), (1, 2)) == False
    assert check_overlap((1, 3), (2, 4)) == False
    assert check_overlap((2, 4), (1, 3)) == False
    assert check_overlap((1, 4), (2, 3)) == False
    assert check_overlap((2, 3), (4, 7)) == True