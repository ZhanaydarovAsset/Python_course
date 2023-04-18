import random

size = int(input('Введите размер списка: '))
array = []
find_numb = int(input(f'поиск числа (от 1 до 10): '))
for i in range (size):
    array.append(random.randint(1, 10))
print(array)
if find_numb - 1 in array:
    print(find_numb - 1)
else:
    print('not')