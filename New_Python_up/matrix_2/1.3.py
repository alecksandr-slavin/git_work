n, m = int(input()), int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for x in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)  # добавление в пустой список

indexis = [int(num) for num in input().split()]
for k in range(len(matrix)):
    for i in indexis[:1]:
        for j in indexis[-1:]:
            matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

for r in range(n):
    for c in range(m):  # проходимя по матрице
        # перед выводом результата переводим в строковый тип данных,
        # и используем функцуию ljust()
        print(str(matrix[r][c]).ljust(3), end='')
    print()
