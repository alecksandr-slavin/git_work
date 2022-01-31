num = input().split()
a = num[-1:]
a.extend(num[:-1])
print(*a)