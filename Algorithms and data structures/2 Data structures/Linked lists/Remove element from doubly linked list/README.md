# УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ ДВУНАПРАВЛЕННОГО СВЯЗНОГО СПИСКА

Сложность: 3 из 10

Добавьте в класс `List` метод `remove` для удаления элементов из двунаправленного связного списка.

Метод должен принимать один аргумент — значение для удаления. 

Не забывайте, устанавливать связи в обе стороны.

**Пример использования**:

```python
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.remove(2)
print(lst.__str__())
[1, 3]
```

Используйте [файл с классами Node и List](#initial.md) как основу для вашего кода.

**[Решение](remove_from_doubly.py)**.