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

    def min(self):
        """
        Минимальное значение в массиве.
        """
        minimal = self.data[0] if self.data else None
        i = 0
        while i < self.length:
            if self.data[i] < minimal:
                minimal = self.data[i]
            i += 1
        return minimal

    def max(self):
        """
        Максимальное значение в массиве.
        """
        maximal = self.data[0] if self.data else None
        i = 0
        while i < self.length:
            if self.data[i] > maximal:
                maximal = self.data[i]
            i += 1
        return maximal

    def avg(self):
        """
        Среднее значение в массиве.
        """
        non_none = [x for x in self.data if x is not None]
        return sum(non_none) / len(non_none)

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


array = Array(4)
array.append(6)
array.append(2)
array.append(1)
array.append(9)
assert array.min() == 1
assert array.max() == 9
assert array.avg() == 4.5

array = Array(6)
array.append(7)
array.append(5)
array.append(9)
array.append(3)
assert array.min() == 3
assert array.max() == 9
assert array.avg() == 6

array = Array(6)
array.append(5)
array.append(5)
array.append(5)
array.append(5)
assert array.min() == 5
assert array.max() == 5
assert array.avg() == 5

array = Array(6)
array.append(9)
assert array.min() == 9
assert array.max() == 9
assert array.avg() == 9


