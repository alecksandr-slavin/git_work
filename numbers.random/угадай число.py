from random import *

print('Приветствую Вас, меня зовут Хатабич, я загадываю числа как школьник и угадываю их')
print('Вам предстоит сиграть в самую крутую игру от создателя iLuminnant')
print()
diapozon = int(input('Выбирите в каком диапазоне хотите угадывать число: от 1 и до '))
number = randint(1, diapozon)


def is_valid(n):
    if not n.isdigit():
        return False
    if not int(n) in range(1, diapozon):
        return False
    return True


def comparable_num():
    new = True
    while new:
        game = True
        total = 0
        while game:
            total += 1
            n = input('Ну ка, угадай какое я число загадал тебе: ')
            if not is_valid(n):
                print(f'А может быть все-таки введем целое число от 1 до {diapozon}?\n')
                continue
            n = int(n)
            if n < number:
                print('Твое число меньше чем у Хатабича, попробуйте еще разок')
                print('ахахахха...')
                print()
            elif n > number:
                print('Твое число больше чем у Хатабича, попробуйте еще разок')
                print('ахахахах...')
                print()
            elif n == number:
                print(f'Оп молодца угадали, число которое загадал Хотабыч\nОтгадали c {total} попытки!')
                print(f'Дед Хотабыч загадал число: {number}')
                print('Спасибо, что сиграли с Хотабычом. Еще увидимся...')
                print('Вжух...\n')
                game = False
        print('Хотели бы еще раз проверить свою силушку против Хотабыча???')
        new_game = input('Если еще порох остался, напишите да или нет: ').lower()
        if new_game == 'да':
            new = True
        else:
            new = False


comparable_num()