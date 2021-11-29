n = int(input())
sok = 0
full = []
for i in range(n):
    s = int(input())
    sok += s
    full.append(sok)
    sok = s
del full[0]
print(full)
