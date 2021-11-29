n, m = int(input()), int(input())  # ввод размера матрицы
matrix = [[0]*m for _ in range(n)] # создание матрицы

total = 0
for x in range(n*m):
    for i in range(n):
        for j in range(m):
            if i + j == x:
                total += 1
                matrix[i][j] = total

for r in range(n):
    for c in range(m):  # проходимя по матрице
        # перед выводом результата переводим в строковый тип данных,
        # и используем функцуию ljust()
        print(str(matrix[r][c]).ljust(3), end='')
    print()