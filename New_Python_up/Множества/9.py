num = input().split()
res = set()
for i in num:
    res.add(i.upper().strip(".,;:-?!"))
print(len(res))