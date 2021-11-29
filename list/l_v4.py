n = [int(i) for i in input().split()]
max1 = n.index(max(n))
min1 = n.index(min(n))
n[max1], n[min1] = n[min1], n[max1]
print(*n)

