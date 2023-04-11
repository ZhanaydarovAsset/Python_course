number = int(input('Введите трехзначное число: '))
summa = 0
while number > 0:
    summa += number % 10
    number //=10 
print(summa)