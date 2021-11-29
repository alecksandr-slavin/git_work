n = int(input())

sok = []
for i in range(n):
    s = input()
    if s not in sok:
        sok.append(s)
print(*sok, sep='\n')