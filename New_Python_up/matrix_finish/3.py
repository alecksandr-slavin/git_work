n = int(input()) # ввод размера матрицы
matrix = [[int(i) for i in input().split()] for _ in range(n)]  # пустой список для матрицы
k = int(input())
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[i][j] ** k

for row in result:
    print(*row)