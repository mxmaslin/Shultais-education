# УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ СТАТИЧЕСКОГО МАССИВА

Сложность: 4 из 10

Запрограммируйте метод `remove` для удаления элементов из статического массива по значению.

Метод должен принимать один аргумент: значение для удаления.

Если в массиве несколько одинаковых элементов подходящих для удаления, то удалять нужно все.

Попробуйте написать алгоритм, который будет работать за время O(N), то есть все манипуляции должны произойти за один проход.

**Пример использования**:

```python
array = Array(5)
array.append(6)
array.append(2)
array.append(1)
array.append(2)
array.append(9)
print(array)
[6, 2, 1, 2, 9]
array.remove(2)
[6, 1, 9]
```

Используйте [файл с классом Array](initial.py) как основу для вашего кода.