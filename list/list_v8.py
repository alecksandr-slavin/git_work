n = int(input())

sok = []
alo = ''
for i in range(n):
    s = input()
    sok.append(s)
k = int(input())
for i in sok:
    if len(i) >= k:
        alo += i[k-1]
print(alo, end='')
