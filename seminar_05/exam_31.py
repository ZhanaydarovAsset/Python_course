n = int(input("n: "))
def Fib(n):
    if n in (0, 1):
        return 1
    return Fib(n - 1) + Fib(n - 2)
print(Fib(n))