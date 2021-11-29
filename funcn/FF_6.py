from math import *


# объявление функции
def solve(a, b, c):
    D = b**2 - 4 * a * c
    x4 = (-b + sqrt(D)) / (2 * a)
    x5 = (-b - sqrt(D)) / (2 * a)
    return min(x4, x5), max(x4, x5)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
