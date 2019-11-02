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


class Stack(Array):
    """
    Двойной стек на базе статического массива.
    """
    def __init__(self, size):
        super().__init__(size)
        self.left_top = -1
        self.right_top = size
        self.size = size


    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.left_top > -1:
            self.length -= 1
            value = self.data[self.left_top]
            self.left_top -= 1
            return value

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        if self.right_top < self.size:
            self.length -= 1
            value = self.data[self.right_top]
            self.right_top += 1
            return value


    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        if self.length >= self.size:
            raise OverflowError

        self.left_top += 1
        self.length += 1
        self.data[self.left_top] = value

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        if self.length >= self.size:
            raise OverflowError

        self.right_top -= 1
        self.length += 1
        self.data[self.right_top] = value

    def clear(self):
        """
        Очищает стек.
        """
        self.left_top = -1
        self.right_top = self.size
        self.length = 0 


class TestLeftExc(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(1)

    def test_raise(self):
        with self.assertRaises(OverflowError):
            self.stack.push_left(1)
            self.stack.push_left(2)


class TestRightExc(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(1)

    def test_raise(self):
        with self.assertRaises(OverflowError):
            self.stack.push_right(1)
            self.stack.push_right(2)


# unittest.main()

stack = Stack(4)
stack.push_left(12)
stack.push_left(7)
stack.push_left(6)
assert stack.pop_left() == 6
assert stack.pop_left() == 7
assert stack.pop_left() == 12

stack = Stack(4)
stack.push_right(12)
stack.push_right(7)
stack.push_right(6)
assert stack.pop_right() == 6
assert stack.pop_right() == 7
assert stack.pop_right() == 12

stack = Stack(6)
stack.push_left(7)
stack.push_right(6)
stack.push_right(2)
stack.push_right(1)
stack.clear()
assert stack.pop_left() == None
assert stack.pop_right() == None


