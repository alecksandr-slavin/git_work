from random import *


def generate_ip():
    return f'{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}'

print(generate_ip())