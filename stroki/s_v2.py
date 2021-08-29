# a, b, c = input(), input(), input()
#
# print(b[0], a[0], c[0], sep='')

####################
a = str(input())

total = 0
for i in range(len(a)):
    total += int(a[i])
print(total)
