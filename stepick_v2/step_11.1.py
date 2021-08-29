a = str(input())
b = str(input())


if a == 'красный' and b == 'синий':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый':
    print('оранжевый')
elif a == 'синий' and b == 'желтый':
    print('зеленый')
elif a == 'красный' and b == 'красный':
    print('красный')
elif a == 'синий' and b == 'синий':
    print('синий')
elif a == 'желтый' and b == 'желтый':
    print('желтый')
else:
    print('ошибка цвета')