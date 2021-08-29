count = 0
total = 1
for i in range(1, 10 + 1):
    x = int(input())
    if x >= 0:
        total *= x
        count += 1
if count > 0:
    print(count, total, sep='\n')
else:
    print('NO')