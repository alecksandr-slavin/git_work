n = int(input())
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером n*n

for i in range(n):
    for j in range(n):# заполняем главную диагональ 1-цами, а побочную 1-ками
        matrix[i][i] = 1
        matrix[i][n-i-1] = 1
        if i < j and i < n - 1 - j:
            # сли элемент находится выше главной диагонали
            matrix[i][j] = 2
        elif i > j and i > n - 1 - j:
            # сли элемент находится ниже главной диагонали
            matrix[i][j] = 3

for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(str(matrix[r][c]).ljust(2), end=' ')
    print()