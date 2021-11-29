# stok, tolb = int(input()), int(input())
# result = []
# ops = []
#
# for i in range(stok * tolb):
#     ops.append(input())
# temp = []
#
#
# for i in ops:
#     temp.append(i)
#     if len(temp) == tolb:
#         result.append(temp)
#         temp = []
#
#
# for r in range(stok):
#     for c in range(tolb):
#         print(result[r][c], end=' ')
#     print()
#
# print()
# for r in range(tolb):
#     for c in range(stok):
#         print(result[c][r], end=' ')
#     print()
#
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()