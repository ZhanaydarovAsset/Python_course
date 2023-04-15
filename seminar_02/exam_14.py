n = int(input("Введите число: "))
m = 2
i = 0
result = 0
while result < n:
    result = m ** i
    i +=1
    if result < n:
        print(result, end = ", ")
