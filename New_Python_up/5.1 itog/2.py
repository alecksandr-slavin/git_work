n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)  # добавление в пустой список

result = []  # создаем пуйстой список
if n == 1:
    for i in matrix:
        print(*i)
else:
    for x in range(n):
        for j in range(n):  # проходимся по матрицы
            if j == n - x - 1:  # добавляем в список result
                result.append(matrix[x][j])
            elif x < j and x > n - 1 - j:  # добавяем в список result
                result.append(matrix[x][j])
            elif x > j and x > n - 1 - j:  # добавяем в список result
                result.append(matrix[x][j])
            elif x + j + 1 > n:  # добавяем в список result
                result.append(matrix[x][j])
    print(max(result))  # выводим на экран