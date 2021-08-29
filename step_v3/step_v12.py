m, n = int(input()), int(input())

p = m + m % 2 - 1
for i in range(p, n-1, -2):
    print(i)
