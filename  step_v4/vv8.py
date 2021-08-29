n = int(input())

max1 = 0
max2 = 0
if n >= 2:
    for i in range(n):
        s = int(input())
        if s > max1:
            max2 = max1
            max1 = s
        elif s > max2:
            max2 = s
print(max1)
print(max2)
