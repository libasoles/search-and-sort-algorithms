from mergeSort import mergeSort

def test_should_sort_an_unsorted_list():
    unsortedData = [15, 3, 29, 43, 54, 12, 16, 10, 8, 45, 99, 32, 75]
    result = mergeSort(unsortedData)
    assert result == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]

def test_should_keep_sorted_lists_sorted():
    unsortedData = [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
    result = mergeSort(unsortedData)
    assert result == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]

def test_should_sort_inverse_lists():
    unsortedData = [99, 75, 54, 45, 43, 32, 29, 16, 15, 12, 10, 8, 3]
    result = mergeSort(unsortedData)
    assert result == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]