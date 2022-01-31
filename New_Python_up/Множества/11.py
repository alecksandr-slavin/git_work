res = [input() for _ in range(int(input()))]
one = set(res[0])
for i in res:
    one.intersection_update(i)
print(*sorted(one))
