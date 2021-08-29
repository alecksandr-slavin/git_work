from math import log


n = int(input())

num = 0
for i in range(1, n+1):
    num += 1 / i
    num2 = num - log(n)
print(num2)