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
    Стек на базе статического массива.
    """

    def __init__(self.size):
        super().__init__(size)
        self.top = -1

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        if self.top >= 0:
            value = self.data[self.top]
            self.top -= 1
            return value


    def push(self, value):
        """
        Кладет элемент со значением value в стек.
        """
        if self.top + 1 == self.size:
            raise OverflowError
        self.top += 1
        self.length += 1
        self.data[self.top] = value


class TestExc(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(3)
        self.stack.push(12)
        self.stack.push(7)
        self.stack.push(6)

    def test_raise(self):
        with self.assertRaises(OverflowError):
            self.stack.push(8)


stack = Stack(3)
stack.push(12)
stack.push(7)
stack.push(6)
assert stack.pop() == 6
assert stack.pop() == 7
assert stack.pop() == 12
assert stack.pop() == None        

# unittest.main()
