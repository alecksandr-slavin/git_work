slov = []
for a in range(int(input())):
    slov.append(input())
    
serch = []
for b in range(int(input())):
    serch.append(input())

res = {}
for i in slov:
    res.setdefault(i[:i.index(':')].lower(), i[i.index(':') + 2:])

for y in serch:
    print(res.get(y.lower(), 'Не найдено'))
