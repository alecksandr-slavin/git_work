a, b = set(map(int, input().split())), set(map(int, input().split()))
c = set(map(int, input().split()))
res = a.intersection(b)
print(*sorted(set(res).difference(c), reverse=True))