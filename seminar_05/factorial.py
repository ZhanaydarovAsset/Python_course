# 1*2*3*4*5
n = int(input("n: "))
def Factor(n):
    if n < 1:
        return 1
    return  n * Factor(n-1)
print(Factor(n))