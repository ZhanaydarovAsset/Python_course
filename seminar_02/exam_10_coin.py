import random
#Вариант 1
# amount_coin = int(input("Введите количество монет: "))
# up = ''
# i = 0
# while i < amount_coin:
#     up += str(random.randint(0, 1))
#     i += 1

# eagle, tail = 0, 0

# for i in range(len(up)):
#     if int(up[i]) > 0:
#         eagle += 1
#     else:
#         tail += 1
# if eagle <= tail:
#     print(eagle)
# else:
#     print(tail)
# print(up)

#Вариант 2

amount_coin = int(input("Введите количество монет: "))
up = 0
i = 0
temp = 0
while i < amount_coin:
    temp = random.randint(0, 1) 
    print(temp, end = " ")
    up += temp
    i += 1
print()
if amount_coin < up*2:
    print(amount_coin - up)
else:
    print(up)
