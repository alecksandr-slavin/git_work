num = int(input())
myset = [input() for _ in range(num)]
res = []
for i in myset:
    res += (i.upper())
print(len(set(res)))