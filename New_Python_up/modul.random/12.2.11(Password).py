import string
from random import *


# Создаем списки букв и цифр
all_letters = string.ascii_letters + string.digits


def refactor_password(leters):
    # Создаем функцию по перебору определеных символов
    res = []
    for i in leters:
        if i not in 'lI1oO0':
            res.append(i)
    return res


def generate_password(length):
    # возвращает случайный пароль длиной length символов
    res = ''
    res += choice(refactor_password(string.ascii_uppercase))
    res += choice(refactor_password(string.digits))
    res += choice(refactor_password(string.ascii_lowercase))
    while len(res) != length:
        res += choice(refactor_password(all_letters))
    return res


def generate_passwords(count):
    # возвращает список, состоящий из count случайных паролей.
    return [generate_password(length_password) for _ in range(count)]


number_password = int(input())  # Количество паролей
length_password = int(input())  # Длина пароля
print(*generate_passwords(number_password), sep='\n')
