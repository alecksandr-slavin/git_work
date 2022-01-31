from random import *
import string


def generate_index():
    A = string.ascii_uppercase
    return f"{choice(A)}{choice(A)}{randint(0, 99)}_{randint(0, 99)}{choice(A)}{choice(A)}"

print(generate_index())