n = int(input())

sok = []
tot = []

for i in range(n):
    sok.append(input())

m = int(input())
for i in range(m):
    tot.append(input())

for s in sok:
    flag = True
    for q in tot:
        if not (q.upper() in s.upper()):
            flag = False
            break
    if flag:
        print(s)