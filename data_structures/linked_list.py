class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def size(self) -> int:
        return self._size

    def add(self, value):
        node = Node(value)
        if self.size() == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._size += 1

    def pop(self):
        if self.size() == 0:
            return None

        if self.size() == 1:
            node = self._head
            self._head = None

            self._size -= 1
            return node.value

        current = self._head
        previous = None
        while current:
            if current.next is None:
                previous.next = None

                self._size -= 1
                return current.value

            previous = current
            current = previous.next

    def get(self, index):
        if index > self._size - 1:
            return None

        if index == 0:
            return self._head.value

        if index == self._size - 1:
            return self._tail.value

        i = 0
        item = None
        current = self._head
        while i < self._size and item is None:
            if i == index:
                item = current

            current = current.next
            i += 1

        return item.value

    def remove(self, index):
        if index > self._size - 1:
            return

        if index == 0:
            self._head = self._head.next
            self._size -= 1
            return

        i = 0
        current = self._head
        previous = None
        while current:
            if i == index:
                previous.next = current.next
                self._size -= 1
                return

            previous = current
            current = previous.next
            i += 1
