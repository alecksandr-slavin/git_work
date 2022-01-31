a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
resulst = a | b
res = c.difference(resulst)
print(*sorted(res, reverse=True))
