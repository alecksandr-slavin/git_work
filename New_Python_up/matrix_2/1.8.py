n = input()  # ввод размера
matrix = [[0]*8 for _ in range(8)]  # создание матрицы списочным выражениям
x = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
y = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
x1, x2 = n[0], n[1]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[y[x2]][x[x1]] = 'N'
        if (y[x2]-i)**2 + (x[x1]-j)**2 == 5:
            matrix[i][j] = '*'
        else:
            matrix[i][j] = '.'

for c in matrix:
    print(*c)
