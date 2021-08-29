n = int(input())
count1 = 1
count2 = 0
for i in range(0, n):
    count2 = count2 + count1
    count1 = count2 - count1
    print(count2, end =" ")
