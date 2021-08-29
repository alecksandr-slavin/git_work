n = int(input())

for x in range(1, n + 1):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    print(x, '+' * count, sep='')