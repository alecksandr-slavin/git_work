numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

result = []
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers[i])):
        count += numbers[i][j]
    result.append(count / len(numbers[i]))
print(result)