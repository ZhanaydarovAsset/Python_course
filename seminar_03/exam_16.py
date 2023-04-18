
import random

size = int(input('Введите размер списка: '))
array = []
find_numb = int(input(f'поиск числа (от 1 до 10)'))
count = 0
for i in range (size):
    array.append(random.randint(1, 10))
for i in array:
    if find_numb == i:
        count += 1

print(count)
print(array)
