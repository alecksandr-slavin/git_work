n = int(input())  # ввод размера матрицы
matrix = [[0]*n for _ in range(n)]  # создание матрицы списочным выражениям
centr = int(n/2)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j or j == n - i - 1:
            matrix[i][j] = '*'
        else:
            matrix[i][j] = '.'

    matrix[i][centr] = '*'
    if i == centr:
        matrix[centr] = '*' * n

for c in matrix:
    print(*c)
