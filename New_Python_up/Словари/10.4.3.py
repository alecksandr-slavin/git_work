a, b = input().lower().replace(' ', ''), input().lower().replace(' ', '')
res, ser = {}, {}
znak = '.,!?:;-'
ls_1 = {res.setdefault(i.strip(znak), a.count(i)) for i in a if i.isalpha()}
ls_2 = {ser.setdefault(i.strip(znak), b.count(i)) for i in b if i.isalpha()}
if res == ser:
    print("YES")
else:
    print('NO')