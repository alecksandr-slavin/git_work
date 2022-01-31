ls = input().split()
symbo = '.,!?:;-'
res = [i.strip(symbo).lower() for i in ls]
result = {}
l = []
for word in res:
    result[word] = result.get(word, 0) + 1

for key, value in result.items():
    if value == min(result.values()):
        l.append(key)

print(min(l))
