num = int(input())
rezult = []
for i in range(num):
    rezult.append(list(range(1, i+2)))

for i in rezult:
    print(i)