class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node(None)

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

