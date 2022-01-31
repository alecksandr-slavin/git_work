a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
res = a & b & c
resulst = a | b | c
print(*sorted(resulst - res))