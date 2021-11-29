n = int(input())
etalon = [i for i in range(1, n * n + 1)]
matr = []
for i in range(n):
    x = list(map(int, input().split()))
    matr.append(x)

col = [0 for _ in range(n)]
row = [0 for _ in range(n)]
dg = 0
dp = 0
tresh = []
for i in range(n):
    for j in range(n):
        tresh.append(matr[i][j])
        col[i] += matr[i][j]
        row[j] += matr[i][j]
        if i == j:
            dg += matr[i][j]
        if i == n - j - 1:
            dp += matr[i][j]

tresh = sorted(tresh)

if col == row and dp == dg and tresh == etalon:
    print('YES')
else:
    print('NO')