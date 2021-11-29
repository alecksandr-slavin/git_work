n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)  # добавление в пустой список

result = []  # создаем пуйстой список
for x in range(n):
    for j in range(n):  # проходимся по матрицы
        if x == j:  # если x = j, то добавляем в список result
            result.append(matrix[x][j])
        elif x < j == n - x - 1:
            result.append(matrix[x][j])
        elif x < j and  x > n - 1 - j:
            result.append(matrix[x][j])
        elif x > j and x < n - 1 - j:  # если x > j, то добавяем в список result
            result.append(matrix[x][j])
print(max(result))  # выводим на экран
