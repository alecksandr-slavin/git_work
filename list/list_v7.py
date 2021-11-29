n = int(input())

sok = []
full = []
for i in range(n):
    s = int(input())
    sok.append(s)
del sok[1::2]
print(sok)
