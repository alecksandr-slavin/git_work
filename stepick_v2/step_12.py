a = int(input())
z = a % 10
x = (a % 100) // 10
c = a // 100

i = max(z, x, c)
p = min(z, x, c)
s = z + x + c - (i + p)
if s == (i - p):
    print('Число интересное')
else:
    print('Число неинтересное')
