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

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        # Добавьте ваш код тут

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        # Добавьте ваш код тут

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        # Добавьте ваш код тут

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        # Добавьте ваш код тут

    def clear(self):
        """
        Очищает стек.
        """
