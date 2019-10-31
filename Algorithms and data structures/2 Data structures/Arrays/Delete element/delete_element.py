class Array:
    """
    Линейный ститический массив.
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

    def remove(self, value):
        found = False
        element_idx = 0
        for i in range(self.length):
            if self.data[i] == value:
                element_idx = i
                found = True
                break

        if found:
            for i in range(element_idx, self.length - 1):
                self.data[i] = self.data[i + 1]

            self.length -= 1
           

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
assert str(array) == '[6, 2, 1, 9]'
array.remove(6)
assert str(array) == '[2, 1, 9]'
array.remove(9)
assert str(array) == '[2, 1]'
array.append(3)
array.remove(1)
assert str(array) == '[2, 3]'
