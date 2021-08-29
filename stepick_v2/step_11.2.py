a = int(input())

if a == 0:
    print('зеленый')
elif a < 0:
    print('ошибка ввода')
elif a <= 10:
    if a % 2:
        print('красный')
    else:
        print('черный')
elif a <= 18:
    if a % 2:
        print('черный')
    else:
        print('красный')
elif a <= 28:
    if a % 2:
        print('красный')
    else:
        print('черный')
elif a <= 36:
    if a % 2:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')