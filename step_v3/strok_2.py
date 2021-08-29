a, b, c = len(input()), len(input()), len(input())

p = a + b + c
i2 = p - (max(a, b, c) + min(a, b, c))
if max(a, b, c) - i2 == i2 - min(a, b, c):
    print('YES')
else:
    print("NO")