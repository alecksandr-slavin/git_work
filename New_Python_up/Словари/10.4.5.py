res, vil = {}, []
for i in range(int(input())):
    s = input().lower().split()
    res.setdefault(s[1], []).append(s[0])

for i in range(int(input())):
    vil.append(input().lower())

for x in vil:
    print(*res.get(x, ['абонент не найден']))
