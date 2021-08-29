from functools import partial


def pow(x, power=1):
    return x ** power


square = partial(pow, power=2)
cube = partial(pow, power=3)