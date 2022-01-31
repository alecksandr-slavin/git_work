a = input().split()
count = a[0]
flag = 'NO'
for i in a:
    if set(i) == set(count):
        flag = "YES"
    else:
        flag = "NO"
print(flag)
