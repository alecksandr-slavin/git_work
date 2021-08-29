from math import factorial


n = int(input())
total = 0
for x in range(1, n+1):
    total += factorial(x)
print(total)