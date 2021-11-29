n = int(input())

sok = []
for i in range(n):
    sok.append(input())
k = input()
for j in sok:
    if k.upper() in j.upper():
        print(j)
