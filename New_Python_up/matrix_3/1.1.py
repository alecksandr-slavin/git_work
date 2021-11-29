n = input()  # ввод размера матрицы
n1, m1 = int(n[:1]), int(n[2:])

matrix = []  # Создаем список, для вложеных списков
for i in range(n1):
    # Создаем пустой список
    result = []
    for j in range(m1):
        # Пороверяем на четность
        if (i + j) % 2 == 0:
            result.append('.')
        else:
            result.append('*')
    # добавляем в основной список
    matrix.append(result)

for x in matrix:
    # Выводим результат
    print(*x)