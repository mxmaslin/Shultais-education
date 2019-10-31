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

    def remove(self, value):
        """
        Удаляет все элементы со значением value.
        Время работы O(N).
        """
        i = 0
        while i < self.length:
            if self.data[i] == value:
                self.data = self.data[:i] + self.data[i+1:]
                self.length -= 1
                i -= 1
            i += 1    


    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


array = Array(5)
array.append(6)
array.append(2)
array.append(1)
array.append(2)
array.append(9)
# array == [6, 2, 1, 2, 9]
array.remove(2)
assert str(array) == '[6, 1, 9]'
array.remove(6)
assert str(array) == '[1, 9]'
array.remove(9)
assert str(array) == '[1]'

array = Array(6)
array.append(7)
array.append(7)
array.append(4)
array.append(5)
array.append(9)
array.append(3)
# array = [7, 7, 4, 5, 9, 3]
array.remove(7)
assert str(array) == '[4, 5, 9, 3]'

array = Array(5)
array.append(7)
array.append(5)
array.append(5)
array.append(9)
array.append(3)
# array == [7, 5, 5, 9, 3]
array.remove(5)
assert str(array) == '[7, 9, 3]'

array = Array(7)
array.append(7)
array.append(7)
array.append(7)
array.append(5)
array.append(9)
array.append(3)
array.append(3)
# array == [7, 7, 7, 5, 9, 3, 3]
array.remove(3)
array.remove(7)
assert str(array) == '[5, 9]'
