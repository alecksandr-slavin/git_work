n, m = [int(i) for i in input().split()]  # ввод размера матрицы
matrix = [[int(i) for i in input().split()] for _ in range(n)]  # пустой список для матрицы
nol = input()
m, k = [int(i) for i in input().split()]  # ввод размера матрицы
matrix_1 = [[int(i) for i in input().split()] for _ in range(m)]
result = [[0] * k for _ in range(n)]

for m in range(m):
    for i in range(n):
        for j in range(k):
            result[i][j] += matrix[i][m] * matrix_1[m][j]

for row in result:
    print(*row)