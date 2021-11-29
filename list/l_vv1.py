s = input()

f = s.count('f')
if f == 1:
    print(-1)
elif f == 0:
    print(-2)
else:
    b = s.find('f') + 1
    print(s.find('f', b))

