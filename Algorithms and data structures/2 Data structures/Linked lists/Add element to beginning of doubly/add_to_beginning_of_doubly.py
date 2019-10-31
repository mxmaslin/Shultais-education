class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def __str__(self):
        return str(self.value)


class List:
    """
    Двунаправленный связный список.
    """

    def __init__(self):
        # Ограничитель
        self.top = Node()

    def append(self, value):
        """
        Добавление нового элемента в конец двунаправленного списка.
        Время работы O(N).
        """

        # Находим последнюю ячейку.
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Вставляем новую ячеку после current и делаем обратную ссылку.
        new_node = Node(value)
        current.next_node = new_node
        new_node.prev_node = current

    def prepend(self, value):
        """
        Добавление нового элемента в начало двунаправленного списка.
        """
        new_node = Node(value)

        # Задаем связи для нового узла
        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top

        # Ставим обратную связь для следующего узла (если он есть)
        # Связь на новый узел.
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        # Меняем ограничитель
        self.top.next_node = new_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


lst = List()
lst.prepend(1)
lst.prepend(2)
lst.prepend(3)
assert str(lst) == '[3, 2, 1]'

lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.prepend(0)
assert str(lst) == '[0, 1, 2, 3]'

lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(5)
lst.append(7)
assert str(lst) == '[1, 2, 3, 5, 7]'
lst.prepend(0)
lst.prepend(-1)
lst.prepend(-2)
assert str(lst) == '[-2, -1, 0, 1, 2, 3, 5, 7]'
zero = lst.top.next_node.next_node.next_node
assert zero.value == 0
assert zero.next_node.value == 1
assert zero.prev_node.value == -1
assert zero.prev_node.prev_node.value == -2
first = lst.top.next_node
assert first.value == -2
assert first.next_node.value == -1
assert first.prev_node.value == None

