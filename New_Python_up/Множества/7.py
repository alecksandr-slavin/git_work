num = int(input())
myset = [input() for _ in range(num)]

for i in myset:
    print(len(set(i.upper())))