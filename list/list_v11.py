n = int(input())

num = []
for i in range(n):
    s = int(input())
    num.append(s)

num.remove((max(num)))
num.remove((min(num)))
print(num)
