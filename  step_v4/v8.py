p = True
for i in range(10):
    s = int(input())
    if s % 2 != 0:
        p = False
if p == True:
    print("YES")
else:
    print('NO')