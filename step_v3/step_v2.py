# m = int(input())
# p = int(input())
# n = int(input())
#
# for i in range(n):
#     m = m + m * p / 100
#     # p = m * (p / 100 + 1) ** i
#     print((i+1), p)
#
m, p, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    print(i, float(m))
    m += m * (p / 100)