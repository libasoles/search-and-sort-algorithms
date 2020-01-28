from algorythms.selection_sort import selection_sort


def test_selection_sort():
    data = [4, 6, 2, 8, 7, 12, 76, 34, 65, 83, 15, 98]
    selection_sort(data)
    assert data == [2, 4, 6, 7, 8, 12, 15, 34, 65, 76, 83, 98]


def test_should_keep_sorted_lists_sorted():
    data = [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
    selection_sort(data)
    assert data == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]


def test_should_sort_inverse_lists():
    data = [99, 75, 54, 45, 43, 32, 29, 16, 15, 12, 10, 8, 3]
    selection_sort(data)
    assert data == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
