class Queue:
    def __init__(self):
        self._items = []

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self.size() == 0

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self._items.pop(0)

    def peek(self):
        if self.size() == 0:
            return None
        return self._items[0]
