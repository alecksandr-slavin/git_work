num = [int(i) for i in input().split()]
if len(num) % 2 == 1:
    r = len(num) - 1
else:
    r = len(num)
for i in range(0, r, 2):
    num[i], num[i + 1] = num[i + 1], num[i]
print(num)