n = int(input())  # ввод размера матрицы
matrix = [[0]*n for _ in range(n)]


for i in range(n):
    for j in range(n):
        # Побочная диагональ
        matrix[i][n - i - 1] = 2
        if i < j and i > n - 1 - j:
            # сли элемент находится выше главной диагонали
            matrix[i][j] = 1
        elif i > j and i > n - 1 - j:
            # сли элемент находится ниже главной диагонали
            matrix[i][j] = 1
        elif i + j + 1 > n:
            # если элемент находится ниже побочной диагонали
            matrix[i][j] = 1
for i in matrix:
    print(*i)
