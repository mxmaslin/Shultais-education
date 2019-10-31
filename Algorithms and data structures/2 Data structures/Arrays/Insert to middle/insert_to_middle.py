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
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def insert(self, position, value):
        """
        Вставляет value на позицию position.
        """
        if self.length == self.size:
            raise OverflowError

        if position > self.length:
            self.append(value)
            return

        self.length += 1

        for i in range(self.length - 1, position, -1):        
            self.data[i] = self.data[i - 1]

        self.data[position] = value



    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class TestOverflowError(unittest.TestCase):
    def setUp(self):
        self.array = Array(1)
        self.array.append(0)

    def test_raise_overflowerror(self):
        with self.assertRaises(OverflowError):
            self.array.insert(1, 1)


class TestIndexError(unittest.TestCase):
    def setUp(self):
        self.array = Array(2)
        self.array.append(0)

    def test_raise_indexerror_big_index(self):
        with self.assertRaises(IndexError):
            self.array.insert(20, 10)

    def test_raise_indexerror_small_index(self):
        with self.assertRaises(IndexError):
            self.array.insert(20, -10)



array = Array(4)
array.append(20)
array.append(10)
array.append(30)
array.insert(1, 40) # вставка на позицию 1
assert str(array) == '[20, 40, 10, 30]'

array = Array(4)
array.append(7)
array.insert(1, 2)
assert str(array) == '[7, 2]'


array = Array(6)
array.append(7)
array.insert(2, 2)
array.insert(8, 9)
assert str(array) == '[7, 2, 9]'



# unittest.main()

# array.insert(2, 50)
# Traceback (most recent call last):
#     ...
# OverflowError
# array.insert(20, 50) # Вставка на несуществующую позицию
# Traceback (most recent call last):
#     ...
# IndexError