ls = input()
res = {}
for i in range(int(input())):
    a, b = input().lower().split(': ')
    res.setdefault(int(b), a)

first = {}
for i in ls:
    first.setdefault(i, ls.count(i))

for x in ls:
    print(res[first[x]], end='')