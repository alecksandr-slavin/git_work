n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)

def checklatin(latin):
    numbers = set(range(1, len(latin) + 1))
    if (any(set(row) != numbers for row in latin) or
            any(set(col) != numbers for col in zip(*latin))):
        print("NO")
    else:
        print("YES")

checklatin(matrix)