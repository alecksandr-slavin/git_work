def chunked(st, num):
    result = []
    temp = []
    for i in st:
        temp.append(i)
        if len(temp) == num:
            result.append(temp)
            temp = []
    if len(st) % num != 0:
        result.append(temp)
    return result


stroka = input().split()
numbr = int(input())
print(chunked(stroka, numbr))
