n = int(input())  # ввод размера
matrix = [input().split() for _ in range(n)]  # создание матрицы списочным выражениям

for c in range(len(matrix)):
    for r in range(len(matrix)):
        print(matrix[::-1][r][c], end=' ')
    print()