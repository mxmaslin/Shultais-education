# ОЧЕРЕДЬ НА БАЗЕ СВЯЗНОГО СПИСКА

Сложность: 3 из 10

Создайте очередь на базе двунаправленного связного списка. Класс для управления очередью должен называться `Queue` и содержать два метода: `enqueue` для добавления новых значений и `dequeue` для извлечения элемента.

В случае если в очереди не осталось элементов, то `dequeue` должен вернуть `None`.

Считаем, что очередь на базе связного списка не ограничена по количеству элементов.

**Пример использования**:

```python
queue = Queue()
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(8)
print(queue.dequeue())
12
print(queue.dequeue())
7
print(queue.dequeue())
6
print(queue.dequeue())
8
print(queue.dequeue())
None
```

Используйте [файл с классами Node и Queue](initial.py) как основу для вашего кода.

**[Решение](linked_list_based_queue.py)**.