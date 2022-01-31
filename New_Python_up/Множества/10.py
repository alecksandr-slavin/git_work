num = [int(i) for i in input().split()]
res = set()
for i in num:
    if i not in res:
        res.add(i)
        print("NO")
    else:
        print("YES")