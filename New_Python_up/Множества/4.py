a, b = input(), input()
ten = set(a + b)
num_10 = set('1234567890')
if ten == num_10:
    print('YES')
else:
    print('NO')