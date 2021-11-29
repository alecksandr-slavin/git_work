from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''  # переменная которая будет содержать все символы, которые могут быть сгенерируемые.

password = int(input('Сколько паролей сгенерировать: '))
range_password = int(input('Какая длина пароля нужна? '))
int_password = input('Включать ли цифры 0123456789&, (y/n)?').lower()
ABC_password = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)').lower()
abc_password = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)').lower()
chOn_password = input('Включать ли символы !#$%&*+-=?@^_? (y/n)').lower()
excOn_password = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)').lower()

if int_password == 'y':
    chars += digits
if ABC_password == 'y':
    chars += uppercase_letters
if abc_password == 'y':
    chars += lowercase_letters
if chOn_password == 'y':
    chars += punctuation
if excOn_password == 'y':
    for i in 'il1Lo0O':
        chars.replace(i, '')


def generate_password(leght, chars):
    return sample(chars, leght)


for _ in range(password):
    print(*generate_password(range_password, chars), sep='')




