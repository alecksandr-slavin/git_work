n = int(input())

num = 1
for row in range(1, n+1):
    for i in range(1, row+1):
        print(num, end=' ')
        num += 1
    print()