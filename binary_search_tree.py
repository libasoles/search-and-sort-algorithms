class Node:

    value = None
    left = None
    right = None

    def __init__(self, value=None):
        self.value = value

    def attach(self, value):

        if not self.value:
            self.value = value
            return

        if value >= self.value:
            if not self.right:
                self.right = Node(value)
                return

            self.right.attach(value)
            return

        if not self.left:
            self.left = Node(value)
            return

        self.left.attach(value)
        return

    def to_list(self, list=[]):

        if self.left:
            self.left.to_list(list)

        list.append(self.value)

        if self.right:
            self.right.to_list(list)

        return list


class Tree:
    main_node = None

    def __init__(self, data):
        self.main_node = Node(None)
        for value in data:
            self.main_node.attach(value)

    def to_list(self):
        return self.main_node.to_list([])

