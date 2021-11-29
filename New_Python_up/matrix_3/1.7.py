n, m = [int(i) for i in input().split()]  # ввод размера матрицы
mtrx = list(range(1, n * m + 1))  # Создаем спискок n*m

def chunked(st, num):
    # создаем 2 пустых списка
    result = []
    temp = []
    for i in st:
        temp.append(i)
        if len(temp) == num:  # проверяем длину списка, с заданой длины матрицы m1
            result.append(temp)
            temp = []  # обнуляем список
    if len(st) % num != 0:
        result.append(*temp)
    for i in range(len(result)):
        if i % 2 != 0:
            result[i].reverse()
    return result

res = chunked(mtrx, m)
for i in range(n):
    for j in range(m):
        print(str(res[i][j]).ljust(3), end='')
    print()