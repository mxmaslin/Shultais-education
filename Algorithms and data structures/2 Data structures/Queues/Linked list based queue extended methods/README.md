# РАСШИРЕННЫЕ МЕТОДЫ ОЧЕРЕДИ НА БАЗЕ СВЯЗНОГО СПИСКА

Сложность: 3 из 10

Расширьте класс `Queue` дополнительными методами:

- `peek()` — должен возвращать значение первого элемента в очереди без его удаления. Если очередь пустая, то peek должен вернуть `None`.
- `count()` — должен возвращать количество элементов в очереди.
- `clear()` — должен очищать очередь.
- 
Также добавьте в очередь контроль размера.

Если очередь полностью заполнена, то очередной вызов `enqueue` должен вернуть исключение `OverflowError`.

**Пример использования**:

```python
queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(6)
...
OverflowError
print(queue.dequeue())
12
print(queue.count())
2
queue.clear()
print(queue.count())
0
print(queue.peek())
None
```

Используйте [файл с классами Node и Queue](initial.py) как основу для вашего кода.

**[Решение](linked_list_based_queue_extended_methods.py)**.