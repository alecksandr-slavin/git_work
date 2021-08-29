n = int(input())

total = 0
for i in range(1, n+1):
    num = (-1) ** (i + 1) * i
    total += num
print(total)
