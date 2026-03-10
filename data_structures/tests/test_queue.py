import unittest

from data_structures.queue import Queue


class TestQueue(unittest.TestCase):
    def test_it_should_have_size_zero_initially(self):
        queue = Queue()
        self.assertEqual(0, queue.size())

    def test_it_should_be_empty_initially(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_it_should_increase_size_when_enqueuing(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(2, queue.size())

    def test_it_should_dequeue_the_first_inserted_value(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(1, queue.dequeue())

    def test_it_should_decrease_size_after_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        self.assertEqual(1, queue.size())

    def test_it_should_return_none_when_dequeuing_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())

    def test_it_should_peek_without_removing(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(10, queue.peek())
        self.assertEqual(2, queue.size())

    def test_it_should_return_none_when_peeking_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.peek())

    def test_it_should_maintain_fifo_order(self):
        queue = Queue()
        for i in range(1, 5):
            queue.enqueue(i)
        result = [queue.dequeue() for _ in range(4)]
        self.assertEqual([1, 2, 3, 4], result)

    def test_it_should_be_empty_after_dequeuing_all_items(self):
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        self.assertTrue(queue.is_empty())
