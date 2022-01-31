n = int(input())
school = [input().split() for _ in range(n)]

for x in school:
    print(*x)

print()

for i in school:
    if int(i[-1]) >= 4:
        print(*i)
