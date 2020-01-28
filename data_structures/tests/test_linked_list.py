import unittest

from data_structures.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_it_should_have_size_zero_initially(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())

    def test_it_should_allow_new_nodes(self):
        linked_list = LinkedList()
        linked_list.add(5)

        self.assertEqual(1, linked_list.size())

    def test_it_retrieves_the_last_inserted_node(self):
        linked_list = LinkedList()
        linked_list.add(3)
        linked_list.add(5)

        self.assertEqual(5, linked_list.pop())
        self.assertEqual(1, linked_list.size())

    def test_it_retrieves_the_last_inserted_node_when_there_is_only_one_item(self):
        linked_list = LinkedList()
        linked_list.add(3)

        self.assertEqual(3, linked_list.pop())
        self.assertEqual(0, linked_list.size())

    def test_it_retrieves_none_when_there_is_no_items(self):
        linked_list = LinkedList()

        self.assertEqual(None, linked_list.pop())
        self.assertEqual(0, linked_list.size())

    def test_it_retrieve_the_searched_item(self):
        linked_list = LinkedList()
        linked_list.add(3)
        linked_list.add(5)
        linked_list.add(7)
        linked_list.add(9)

        item = linked_list.get(2)

        self.assertEqual(7, item)

    def test_it_retrieve_the_searched_item_when_there_is_only_one_item(self):
        linked_list = LinkedList()
        linked_list.add(3)

        item = linked_list.get(0)

        self.assertEqual(3, item)

    def test_it_retrieves_none_when_there_is_no_items(self):
        linked_list = LinkedList()
        item = linked_list.get(0)

        self.assertEqual(None, item)

    def test_it_retrieves_none_when_the_index_is_higher_than_link_size(self):
        linked_list = LinkedList()
        linked_list.add(3)
        linked_list.add(5)
        linked_list.add(7)
        linked_list.add(9)

        item = linked_list.get(5)

        self.assertEqual(None, item)

    def test_it_removes_an_item_correctly(self):
        linked_list = LinkedList()
        linked_list.add(3)
        linked_list.add(5)
        linked_list.add(7)
        linked_list.add(9)

        linked_list.remove(2)

        self.assertEqual(3, linked_list.size())
        self.assertEqual(9, linked_list.get(2))

    def test_it_removes_nothing_if_index_is_higher_than_list_size(self):
        linked_list = LinkedList()
        linked_list.add(3)
        linked_list.add(5)
        linked_list.add(7)
        linked_list.add(9)

        linked_list.remove(5)

        self.assertEqual(4, linked_list.size())
