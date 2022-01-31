matrix = [['.'] * 8 for _ in range(8)]
a, b = list(input())
x = 8 - int(b)
y = ord(a) - 97

for i in range(8):
    for j in range(8):
        if (i != x or j != y)\
                and ((i == x or j == y) or
                    (abs(i - x) == abs(j - y))):
            matrix[i][j] = '*'
        matrix[x][y] = 'Q'
for row in matrix:
    print(*row)