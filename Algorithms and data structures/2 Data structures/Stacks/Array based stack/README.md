# СТЕК НА БАЗЕ СТАТИЧЕСКОГО МАССИВА

Сложность: 2 из 10

Создайте стек на базе статического массива. Класс для управления стеком должен называться `Stack` и содержать два метода: `push` для добавления новых значений и `pop` для извлечения верхнего элемента.

В случае если в стеке не осталось элементов, то `pop` должен вернуть `None`.

Если стек полностью заполнен, то очередной вызов `push` должен вернуть исключение `OverflowError`.

Пример использования:

```python
stack = Stack(3)
stack.push(12)
stack.push(7)
stack.push(6)
stack.push(8)
...
OverflowError
print(stack.pop())
6
print(stack.pop())
7
print(stack.pop())
12
print(stack.pop())
None
```

Используйте [файл с классами Array и Stack](initial.py) как основу для вашего кода.