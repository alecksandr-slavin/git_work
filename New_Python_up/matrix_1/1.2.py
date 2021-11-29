n = int(input())
matrix = []
result = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
for i in range(n):
    result += matrix[i][i]
print(result)
