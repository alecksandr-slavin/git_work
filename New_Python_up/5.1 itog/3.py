n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)


for r in range(n):
    for c in range(n):
        print(str(matrix[c][r]).ljust(2), end=' ')
    print()