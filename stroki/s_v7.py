n = int(input())

total = ''
while n != 0:
    total = str(n % 2) + total
    n //= 2
print(total)