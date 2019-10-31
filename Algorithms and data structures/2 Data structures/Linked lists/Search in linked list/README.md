# Поиск в связном списке

Сложность: 2 из 10

Ячейка связного списка принимает два значения: `key` и `value`:

``` python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.key, self.value
```

Создайте метод `find`, который ищет ячейку в связном списке по значению `key` и возвращает `value`.

Если элемента с искомым `key` в списке нет, метод должен возвращать `None`.

**Пример использования**:

```python
lst = List()
lst.append(1, "A")
lst.append(2, "B")
lst.append(3, "C")
lst.append(4, "D")
print(lst.find(3))
C
print(lst.find(5))
None
```

Используйте [файл с классами Node и List](initial.py) как основу для вашего кода.