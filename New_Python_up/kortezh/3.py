a, b, c = int(input()), int(input()), int(input())
result = []
res = ((4 * a * c) - (b * b)) / (4 * a)
tap = -b / (2 * a)
result.append(tap)
result.append(res)
print(tuple(result))
