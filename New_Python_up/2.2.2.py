num = [int(n) for n in input().split()]
counter = 0

for i in range(1, len(num)):
    if num[i] > num[i - 1]:
        counter += 1

print(counter)