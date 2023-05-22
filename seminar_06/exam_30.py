#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

first_num = int(input("Введите первое число: "))
difference = int(input("введите разность: "))
amount = int(input("введите количество элементов: "))
array = [first_num]
for i in range(amount-1):
    array.append(array[-1] + difference)
print(array)

def f(first_num, difference, amount):
    return [first_num + i*difference for i in range (amount)]

print(f(1,2,10))