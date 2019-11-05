import unittest


class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Queue(Array):
    """
    Очередь на базе статического массива.
    """
    def __init__(self, size):
        super().__init__(size)
        self.last = -1
        self.first = 0

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        if self.length == self.size:
            raise OverflowError

        self.last = (self.last + 1) % self.size
        self.data[self.last] = value
        self.length += 1


    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if self.length:
            value = self.data[self.first]
            self.first = (self.first + 1) % self.size
            self.length -= 1
            return value
        return None


class TestExc(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)

    def test_raise(self):
        with self.assertRaises(OverflowError):
            self.queue.enqueue(12)
            self.queue.enqueue(7)
            self.queue.enqueue(6)
            self.queue.enqueue(3)


# unittest.main()

queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
# queue.enqueue(8)
# ...
# OverflowError
assert queue.dequeue() == 12
assert queue.dequeue() == 7
assert queue.dequeue() == 6
assert queue.dequeue() == None

queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
assert queue.dequeue() == 12
queue.enqueue(8)
assert str(queue) == '[8, 7, 6]'
assert queue.dequeue() == 7
