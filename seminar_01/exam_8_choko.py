"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками
 (то есть разломить шоколадку на два прямоугольника).
 """

n = int(input("размер шоколада (n): "))
m = int(input("размер шоколада (m): "))
k = int(input("сколько хочешь долек: "))
if k >= n or k >= m:
    if k % n == 0 or k % m == 0:
        print(f"шоколад с размерами {n}Х{m} можно отломит {k} долек")
else:
    print("нельзя")