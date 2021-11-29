n, m = int(input()), int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for x in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)

maxon = []  # создаем пустой список для максимов
for r in matrix:  # проходимя по матрице
    maxon.append(max(r))  # добавляем в пустой список максимим, аждого вложенного списка

max1 = max(maxon)  # находим максимум данного списка
st = maxon.index(max1)  # находим индекс данного максимума столбца
st2 = matrix[st].index(max1)  # находим индекс данного максмума строки
print(st, st2)  # выводим
