stroka = input().split('О')
total = []
for i in stroka:
    total.append(len(i))
print(max(total))