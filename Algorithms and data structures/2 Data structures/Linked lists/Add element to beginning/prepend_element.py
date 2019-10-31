class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)

    def prepend(self, value):
        first_node = Node(value)
        self.head, self.head.next_node = first_node, self.head
        

    def __str__(self):
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


lst = List()
lst.append('A')
lst.append('B')
lst.prepend('C')
lst.prepend('D')
assert str(lst) == '[D, C, A, B]'

lst = List()
lst.append('A')
assert str(lst) == '[A]'

lst = List()
lst.prepend(1)
lst.prepend(2)
lst.prepend(3)
lst.prepend(4)
assert str(lst) == '[4, 3, 2, 1]'


lst = List()
lst.prepend(0)
lst.prepend(-1)
lst.prepend(-2)
lst.prepend(-3)
assert str(lst) == '[-3, -2, -1, 0]'
