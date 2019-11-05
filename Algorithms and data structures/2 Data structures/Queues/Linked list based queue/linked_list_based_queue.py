class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node(None)
        self.first = None

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value)
        
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top
        self.top.next_node = new_node

        if not self.first:
            self.first = new_node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if self.first:
            value = self.first.value
            self.first = self.first.prev_node
            self.first.next_node = None

            if self.first.value is None:
                self.first = None            

            return value


queue = Queue()
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(8)
assert queue.dequeue() == 12
assert queue.dequeue() == 7
assert queue.dequeue() == 6
assert queue.dequeue() == 8
assert queue.dequeue() == None

queue = Queue()
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(1)
assert queue.dequeue() == 7
assert queue.dequeue() == 6
assert queue.dequeue() == 2
assert queue.dequeue() == 1
assert queue.dequeue() == None
queue.enqueue(13)
queue.enqueue(9)
assert queue.dequeue() == 13
