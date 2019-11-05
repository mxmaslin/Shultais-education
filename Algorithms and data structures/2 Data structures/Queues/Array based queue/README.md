# ОЧЕРЕДЬ НА БАЗЕ СТАТИЧЕСКОГО МАССИВА

Сложность: 4 из 10

Создайте очередь на базе статического массива. Класс для управления очередью должен называться `Queue` и содержать два метода: `enqueue` для добавления новых значений и `dequeue` для извлечения элемента.

В случае если в очереди не осталось элементов, то `dequeue` должен вернуть `None`.
Если очередь полностью заполнена, то очередной вызов `enqueue` должен вернуть исключение `OverflowError`.

**Пример использования**:

```python
queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(8)
...
OverflowError
print(queue.dequeue())
12
print(queue.dequeue())
7
print(queue.dequeue())
6
print(queue.dequeue())
None
```

Используйте [файл с классами Array и Queue](initial.py) как основу для вашего кода.

**[Решение](array_based_queue.py)**.
