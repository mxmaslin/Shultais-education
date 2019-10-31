def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    array1 и array2 - массивы представленные python-списками.
    """
    merged = []
    while array1 and array2:
        if array1[0] <= array2[0]:
            merged.append(array1[0])
            array1 = array1[1:]
        else:
            merged.append(array2[0])
            array2 = array2[1:]
        if not (array1 and array2):
            remainer = array1 if array1 else array2
            merged += remainer
    if not merged:
        return array1 if len(array1) >= len(array2) else array2
    return merged


array1 = [3, 4, 7, 8]
array2 = [1, 5, 9]
array = merge(array1, array2)
assert array == [1, 3, 4, 5, 7, 8, 9]

array1 = [3, 4, 7, 8]
array2 = [70]
array = merge(array1, array2)
assert array == [3, 4, 7, 8, 70]

array1 = [3, 4, 7, 8]
array2 = [50, 70]
array = merge(array1, array2)
assert array == [3, 4, 7, 8, 50, 70]

array1 = [1]
array2 = [50, 70]
array = merge(array1, array2)
assert array == [1, 50, 70]

array1 = [1, 1]
array2 = [1, 50, 70]
array = merge(array1, array2)
assert array == [1, 1, 1, 50, 70]

array1 = []
array2 = [1, 50, 70]
array = merge(array1, array2)
assert array == [1, 50, 70]

array1 = []
array2 = []
array = merge(array1, array2)
assert array == []


