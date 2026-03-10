import unittest

from data_structures.stack import Stack


class TestStack(unittest.TestCase):
    def test_it_should_have_size_zero_initially(self):
        stack = Stack()
        self.assertEqual(0, stack.size())

    def test_it_should_be_empty_initially(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_it_should_increase_size_when_pushing(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.size())

    def test_it_should_pop_the_last_pushed_value(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.pop())

    def test_it_should_decrease_size_after_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertEqual(1, stack.size())

    def test_it_should_return_none_when_popping_empty_stack(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_it_should_peek_without_removing(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(20, stack.peek())
        self.assertEqual(2, stack.size())

    def test_it_should_return_none_when_peeking_empty_stack(self):
        stack = Stack()
        self.assertIsNone(stack.peek())

    def test_it_should_not_be_empty_after_push(self):
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_it_should_be_empty_after_popping_all_items(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        self.assertTrue(stack.is_empty())
