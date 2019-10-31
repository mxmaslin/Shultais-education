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

    def reverse(self):
        """
        Разворачивает массив.
        """
        half_arr_length = self.length // 2
        for i in range(half_arr_length):
            self.data[i], self.data[self.length-i-1] = self.data[self.length-i-1], self.data[i] 


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
array.reverse()
assert str(array) == '[9, 1, 2, 6]'

array = Array(5)
array.append(6)
array.append(2)
array.append(1)
array.append(9)
array.append(10)
array.reverse()
assert str(array) == '[10, 9, 1, 2, 6]'
