n = int(input())

num = []
total = []

for i in range(n):
    s = int(input())
    num.append(s)
    total.append(s ** 2 + (2 * s) + 1)
print(*num, sep='\n')
print()
print(*total, sep='\n')