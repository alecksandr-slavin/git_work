# from math import sqrt
#
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# s = sqrt((a - c)**2 + (b - d)**2)
# print(s)
################
# from math import pi
# a = float(input())
# s = pi * a**2
# c = 2 * pi * a
# print(s)
# print(c)
#############
# from math import sqrt
# a = float(input())
# b = float(input())
#
# z = (a + b) / 2
# x = sqrt(a * b)
# c = (2 * a * b) / (a + b)
# v = sqrt((a**2 + b**2) / 2)
# print(z, x, c, v, sep='\n')
#################
# from math import *
# x = float(input())
#
# r = (x * pi) / 180
# sum = sin(r) + cos(r) + (tan(r) * tan(r))
# print(sum)
#################
# from math import ceil, floor
# a = float(input())
# print(ceil(a) + floor(a))
#
# from math import *
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# D = b**2 - 4 * a * c
# if D < 0:
#     print("Нет корней")
# elif D == 0:
#     x = -b / 2 * a
#     print(x)
# elif D > 0:
#     x1 = (-b + sqrt(D)) / 2 * a
#     x2 = (-b - sqrt(D)) / 2 * a
#     print(min(x1, x2), max(x1, x2), sep='\n')
# from math import *
# n = int(input())
# a = float(input())
#
# s = (n * a ** 2) / (4 * tan(pi / n))
# print(s)