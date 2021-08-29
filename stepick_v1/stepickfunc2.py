a = input().lower().split()
s = set(a)
for x in s:
    print(x + ' ' + str(a.count(x)))
