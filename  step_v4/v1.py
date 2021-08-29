a = int(input())
b = int(input())
if a > b:
    a, b = b, a

total = 0
for i in range(a, b+1):
    if i ** 3 % 10 in (4, 9):
        total += 1
print(total)
