a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
x = set(range(11))
resulst = a | b | c
res = x.difference(resulst)
print(*sorted(res))
