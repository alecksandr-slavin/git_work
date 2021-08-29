n = input()

total_0 = 0
total_plus = 0
for i in range(len(n)):
    if n[i] == '*':
        total_0 += 1
    elif n[i] == '+':
        total_plus += 1
print('Символ + встречается', total_plus, 'раз')
print('Символ * встречается', total_0, 'раз')