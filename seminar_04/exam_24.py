import random

bush_quantity = int(input("количество кустов: "))
bed = list()
for i in range(bush_quantity):
    bed.append(random.randint(1,10))
print(bed)
max = 0
sum = 0
for j in range(len(bed)):
    try:
        sum = bed[j-1] + bed[j] + bed[j+1]
    except IndexError:
        sum = bed[j-1] + bed[j] + bed[0]
    except Exception:
        sum = bed[-1] + bed[j] + bed[j+1]
        # if j == len(bed)-1:
    if sum > max:
        max = sum
print(max)
