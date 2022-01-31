n = int(input()) # ввод размера матрицы
matrix = [[int(i) for i in input().split()] for _ in range(n)]  # пустой список для матрицы
k = int(input())
res = matrix[:]

def matr_x(mtrxA, mtrxB, num):
    result = [[0] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            for q in range(num):
                result[i][j] += mtrxA[i][q] * mtrxB[q][j]
    return result

for x in range(k - 1):
    res = matr_x(matrix, res, n)

for row in res:
    print(*row)