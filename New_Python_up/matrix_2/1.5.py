n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for x in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)  # добавление в пустой список

for i in range(len(matrix)):  # Проходимся по матрице и делаем присваевание
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]

for r in matrix:  # выводим матрицу
    print(*r)

# new_matrix = matrix[::-1]  # Делаем срез в обратную сторону
# for i in new_matrix:  # Проходися по новому списку
#     print(*i)  # Выводим