from insertion_sort import insertion_sort


def test_should_sort_a_tiny_list():
    unsorted_data = [3, 2, 7]
    result = insertion_sort(unsorted_data)
    assert result == [2, 3, 7]


def test_should_sort_an_unsorted_list():
    unsorted_data = [15, 3, 29, 43, 54, 12, 16, 10, 8, 45, 99, 32, 75]
    result = insertion_sort(unsorted_data)
    assert result == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]


def test_should_keep_sorted_lists_sorted():
    unsorted_data = [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
    result = insertion_sort(unsorted_data)
    assert result == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]


def test_should_sort_inverse_lists():
    unsorted_data = [99, 75, 54, 45, 43, 32, 29, 16, 15, 12, 10, 8, 3]
    result = insertion_sort(unsorted_data)
    assert result == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
