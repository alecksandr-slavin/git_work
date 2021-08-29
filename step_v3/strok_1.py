a, b, c = input(), input(), input()
z = len(a)
x = len(b)
s = len(c)
p = max(z, x, s)
i = min(z, x, s)
if i == z:
    print(a)
elif i == x:
    print(b)
elif i == s:
    print(c)
if p == z:
    print(a)
elif p == x:
    print(b)
elif p == s:
    print(c)
