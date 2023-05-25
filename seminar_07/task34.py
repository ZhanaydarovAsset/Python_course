rythm = 'пара-ра-рам рам-пам-папам па-ра-па-да'
key = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
lRythm = rythm.split()
result = list()
for w in lRythm:
    count = 0
    for s in w:
        if s in key:
            count +=1
            result.append(count)
if len(set(result)) == 1:
    print('Парам пам-пам')
else: print('Пам парам')