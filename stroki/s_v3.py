n = input()
flag = ''
for i in range(len(n)):
    if n[i] in '0123456789':
        flag = 'Цифра'
        break
    else:
        flag = 'Цифр нет'
print(flag)