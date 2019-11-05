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

    def __init__(self, size):
        self.top = Node(None)
        self.first = None
        self.size = size

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value)

        # Вставялем элемент в начало.

        # Связываем последний элемент в очереди с новым.
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        # Связываем новый элемент со следующим (последним) и с top.
        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top

        # Связываем top с новым.
        self.top.next_node = new_node

        # Устанавливаем first, если это первая вставка.
        if not self.first:
            self.first = new_node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """

        # Если элемент есть, то получаем его значение.
        if self.first:
            value = self.first.value

            # Смещаем указатель.
            self.first = self.first.prev_node

            # Удаляем последний элемент.
            self.first.next_node = None

            # Проверяем, не ссылается ли first на top.
            # Если ссылается, то сбрасываем first.
            if self.first.value is None:
                self.first = None

            return value

        return None

    def count(self):
        """
        Возвращает количество элементов в очереди.
        """
        # Добавьте ваш код тут.

    def peek(self):
        """
        Возвращает значение первого элемента очереди без его извлечения.
        """
        # Добавьте ваш код тут.

    def clear(self):
        """
        Очищает очередь.
        """
        # Добавьте ваш код тут.

