a = int(input())
b = int(input())

total_max = 0
max_x = 0

for x in range(a, b + 1):
    count = 0
    for i in range(1, b + 1):
        if x % i == 0:
            count += i
        if count >= total_max:
            total_max = count
            max_x = x
            count = 0
print(max_x, total_max, end=' ')