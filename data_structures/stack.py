class Stack:
    def __init__(self):
        self._items = []

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self._items.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self._items[-1]
