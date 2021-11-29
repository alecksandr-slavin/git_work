lip = input().split()
ops = lip[:1]
result = [ops]
for i in range(1, len(lip)):
    if lip[i-1] == lip[i]:
        result[-1].extend(lip[i-1])
    else:
        result.append([lip[i]])
print(result)