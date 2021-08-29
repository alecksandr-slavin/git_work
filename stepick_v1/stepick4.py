s = [int(i) for i in input().split()]
l = len(s) - 1
s = list(s)
t = ''
# if len(s) == 1:
#     t = t + s + str(c)
# else:
for i in range(0, l):
    if s[i] == s[i + 1]:
        c += 1
    elif s[i] != s[i + 1]:
        t = t + s[1]
for j in range(l, l + 1):
    if s[-1] == s[-2]:
        t = t + s[j]
    elif s[-1] != s[-2]:
        t = t + s[j]
print(t.sort())
