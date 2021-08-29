a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    print('\t', i, end='')
print('\n')
for j in range(a, b + 1):
    print(j, end='')
    for g in range(c, d + 1):
        print('\t', g * j, end='')
    print()
