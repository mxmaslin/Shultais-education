# ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ В КОНЕЦ СТАТИЧЕСКОГО МАССИВА

Сложность: 2 из 10

На базе класса `Array` нужно реализовать метод `append` для вставки элементов в конец массива.

Метод должен принимать один аргумент — значение для вставки.

В случае если массив полностью заполнен, при добавлении нового значения должно срабатывать исключение `OverflowError`.

**Пример использования**:

```python
array = Array(3)
print(array.size)
3
print(array.length)
0
print(array)
[]
array.append(20)
array.append(10)
array.append(30)
print(array)
[20, 10, 30]
array.append(40)
Traceback (most recent call last):
    ...
OverflowError
```

[Класс Array](initial.py)

**[Решение](add_element_to_end.py)**.
