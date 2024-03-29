# РАСШИРЕННЫЕ МЕТОДЫ СТЕКА НА БАЗЕ СВЯЗНОГО СПИСКА

Сложность: 2 из 10

Расширьте класс `Stack` дополнительными методами:

- `peek()` — должен возвращать верхний элемент в стеке без его удаления.
Если стек пустой, то `peek` должен вернуть `None`.
- `count()` — должен возвращать количество элементов в стеке.
- `clear()` — должен очищать стек.

**Пример использования**:

```python
stack = Stack()
stack.push(12)
stack.push(7)
stack.push(6)
print(stack.peek())
6
print(stack.count())
3
stack.clear()
print(stack.count())
0
print(stack.peek())
None
```

Используйте [файл с классами Node и Stack](initial.py) как основу для вашего кода.

**[Решение](extended_stack_methods.py)**.