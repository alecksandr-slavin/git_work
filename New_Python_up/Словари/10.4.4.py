res = {}
for i in range(int(input())):
    s = input().split()
    res.setdefault(s[0], s[1])
sis = input()
for a, b in res.items():
    if sis in a:
        print(b)
    elif sis in b:
        print(a)
