result = {}
for i in range(1, 16):
    a = result.setdefault(i, i**2)
print(result)