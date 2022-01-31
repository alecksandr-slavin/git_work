ltz = input().split()
n = int(input())
rezult = []
for i in range(n):
    rezult.append(ltz[i::n])
print(rezult)