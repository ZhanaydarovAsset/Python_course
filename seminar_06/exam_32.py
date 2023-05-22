# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def check_value(arr, min, max):
    indexes = list()
    for i in range(min, max+1):
        if i in arr:
            indexes.append(arr.index(i))
    indexes.sort()
    return indexes


array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(check_value(array, 1, 10))

def f(array, min, max):
    return list(idx for idx, x in enumerate(array) if min <= x <= max)

print(f(array, 1,10))
