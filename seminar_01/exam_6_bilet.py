import random
numb_ticket = random.randint(100_000, 999_999)
left_numb = numb_ticket // 1000
right_numb = numb_ticket % 1000

def summa_numer (numb):
    summa = 0
    while numb > 0:
        summa += numb % 10
        numb //=10 
    return summa

l_sum = summa_numer(left_numb)
r_sum = summa_numer(right_numb)
print(numb_ticket, l_sum == r_sum)