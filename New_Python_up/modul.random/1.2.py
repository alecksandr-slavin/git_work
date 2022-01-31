from random import *

length = int(input())    # длина пароля

digits = 'abcdefghijklmnopqrstuvwxyz' \
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_password(leght, digits):
    return sample(digits, leght)

print(*generate_password(length, digits), sep='')
# for i in range(length):
#     print(chr(randint(65, 90)), chr(randint(97, 122)), end='')