num = int(input())
ops = []
result = 'НЕТ'
for i in range(num):
    ops.append(int(input()))

big = int(input())
for p in range(num - 1):
    for j in range(p + 1, num):
        if ops[p] * ops[j] == big:
            result = 'ДА'
            break
print(result)