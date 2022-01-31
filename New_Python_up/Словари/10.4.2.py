a, b = input(), input()
res, ser = {}, {}
ls_1 = {res.setdefault(i, a.count(i)) for i in a}
ls_2 = {ser.setdefault(i, b.count(i)) for i in b}
if res == ser:
    print("YES")
else:
    print('NO')