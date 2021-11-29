n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for x in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)  # добавление в пустой список
flag = 'YES'
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i] != matrix[j]:
            if matrix[i][j] != matrix[j][i]:
                flag = 'NO'
                break
print(flag)
