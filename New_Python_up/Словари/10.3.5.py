ls = input().split()
res = []
for i in ls:
    if not i in res:
        res.append(i)
        print(i, end=' ')
    else:
        print(f"{i}_{res.count(i)}", end=' ')
        res.append(i)

