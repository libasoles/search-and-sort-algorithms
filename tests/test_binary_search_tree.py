from ..binary_search_tree import Tree


def test_binary_search_tree_sort():
    unsorted_data = [94, 35, 12, 47, 65, 21, 18, 9, 88, 75, 32]
    tree = Tree(unsorted_data)
    assert tree.to_list() == [9, 12, 18, 21, 32, 35, 47, 65, 75, 88, 94]


def test_should_keep_sorted_lists_sorted():
    unsorted_data = [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
    tree = Tree(unsorted_data)
    assert tree.to_list() == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]


def test_should_sort_inverse_lists():
    unsorted_data = [99, 75, 54, 45, 43, 32, 29, 16, 15, 12, 10, 8, 3]
    tree = Tree(unsorted_data)
    assert tree.to_list() == [3, 8, 10, 12, 15, 16, 29, 32, 43, 45, 54, 75, 99]
