n = int(input())  # ввод размера
matrix = [input().split() for _ in range(n)]  # создание матрицы списочным выражениям

for i in matrix[::-1]:
    print(*i)