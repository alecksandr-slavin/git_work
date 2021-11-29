n = input()
r = n[1:]
total = []
for i in range(int(r)):
    s = input()
    if '#' not in s:
        total.append(s)
    if '#' in s:
        s.find('#')
        m = s[:s.index('#')].rstrip()
        total.append(m.rstrip())
print(*total, sep='\n')
