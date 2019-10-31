import unittest


class Array:
    """
    Линейный статический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполненного массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length >= self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1
        

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class TestExc(unittest.TestCase):
    def setUp(self):
        self.array = Array(1)
        self.array.append(0)

    def test_raise(self):
        with self.assertRaises(OverflowError):
            self.array.append(1)


array = Array(3)
assert array.size == 3
assert array.length == 0
assert str(array) == '[]'

array.append(20)
array.append(10)
array.append(30)

assert str(array) == '[20, 10, 30]'

unittest.main()

# array.append(40)
# Traceback (most recent call last):
#     ...
# OverflowError
