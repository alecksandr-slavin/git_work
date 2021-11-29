n = int(input())

total = []
finish = []
for i in range(n):
    total.append(int(input()))
for i in total:
    if i < 0:
        finish.append(i)
for i in total:
    if i == 0:
        finish.append(i)
for i in total:
    if i > 0:
        finish.append(i)
print(*finish, sep='\n')