from random import *


mat = list(range(1, 76))
shuffle(mat)
def chunked(sp, n):
    return [sp[x:x + n] for x in range(0, len(sp), n)]

matrix = chunked(mat, 5)
matrix[2][2] = 0
for r in range(5):
    for c in range(5):
        print(str(matrix[r][c]).ljust(3), end='')
    print()