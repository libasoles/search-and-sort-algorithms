from ..binary_search import binary_search


def test_should_find_a_result_in_a_tiny_array():
    data = [2, 3, 5]
    target = 5
    result = binary_search(data, target)
    assert result == target


def test_should_find_a_result_in_a_small_array():
    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 67
    result = binary_search(data, target)
    assert result == target


def test_should_find_a_result_that_is_last_in_the_row():
    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 97
    result = binary_search(data, target)
    assert result == target


def test_should_not_find_a_result_if_element_is_not_in_the_list():
    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 40
    result = binary_search(data, target)
    assert result == -1
