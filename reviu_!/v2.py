max1 = -10001
summ = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        summ += x
    elif 0 > x > max1:
        max1 = x
if summ < 0:
    print(summ, max1, sep='\n')
else:
    print('NO')