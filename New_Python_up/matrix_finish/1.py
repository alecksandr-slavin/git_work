n, m = [int(i) for i in input().split()]  # ввод размера матрицы
matrix = [[int(i) for i in input().split()] for _ in range(n)]  # пустой список для матрицы
nol = input()
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = matrix[i][j] + matrix_1[i][j]

for r in range(n):
    for c in range(m):  # проходимя по матрице
        # перед выводом результата переводим в строковый тип данных,
        # и используем функцуию ljust()
        print(str(result[r][c]).ljust(2), end='')
    print()