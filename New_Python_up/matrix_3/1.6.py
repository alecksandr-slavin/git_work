n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()