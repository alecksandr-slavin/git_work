n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'NO'
res = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


m = 0
for i in range(1, n):
    k = 0
    for j in range(i):
        if (matrix[i][j] == matrix[j][i]):
            k = k+1
    if k == i:
        m = m+1
if (m == n-1):
    print('YES')
else:
    print('NO')