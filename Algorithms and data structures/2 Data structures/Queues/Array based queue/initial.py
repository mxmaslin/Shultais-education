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

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        # Добавьте ваш код тут

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        # Добавьте ваш код тут
