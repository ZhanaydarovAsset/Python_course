# s = x+y
# p = x*y
# p = x*s - x*x
# x*x -s*x + p = 0
# D = s**2 - 4*p -> x = s +- D**0.5 / 2

x = int(input("загадайте первое число до 1000: "))
y = int(input("загадайте второе число до 1000: "))
help_1 = x + y
help_2 = x * y

D = help_1**2 - 4*help_2
print(D)
a = (help_1 + D**0.5) / 2
b = (help_1 - D**0.5) / 2
print(a, b)

