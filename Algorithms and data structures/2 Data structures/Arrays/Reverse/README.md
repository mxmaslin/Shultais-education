РАЗВОРОТ МАССИВА

Сложность: 2 из 10

Добавьте в массив `Array` метод `reverse`, который развернет массив в обратном порядке.

Сложность такого алгоритма будет O(N), однако на практике нужно пройти только половину массива, меняя на каждом шаге два элемента (слева и справа).

**Пример использования**:

``` python
array = Array(4)
array.append(6)
array.append(2)
array.append(1)
array.append(9)
print(array)
[6, 2, 1, 9]
array.reverse()
print(array)
[9, 1, 2, 6]
```

Используйте [файл с классом Array](initial.py) как основу для вашего кода.

**[Решение](reverse.py)**.