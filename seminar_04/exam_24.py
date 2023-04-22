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
    
    if sum > max:
        max = sum
print(max)

# arr = list()
# for i in range(len(bed) - 1):
#     arr.append(bed[i-1]+ bed[i] + bed[i+1])
# arr.append(bed[-2]+bed[-1]+bed[0])
# print(max(arr))