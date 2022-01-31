# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82',
#            '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29',
#            '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16',
#            '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62',
#            '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38',
#            '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25',
# #            '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# #
# # for i in numbers:
# #     num = Fraction(i)
# #     print(f"{i} = {num}")
# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57' \
#     ' 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02' \
#     ' 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24' \
#     ' 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# res = [Fraction(i) for i in s.split()]
# print(sum((max(res), min(res))))
# from fractions import Fraction as F
#
# m, n = input(), input()
# a = F(m) + F(n)
# b = F(m) - F(n)
# c = F(m) * F(n)
# d = F(m) / F(n)
# print(f'{m} + {n} = {a}')
# print(f'{m} - {n} = {b}')
# print(f'{m} * {n} = {c}')
# print(f'{m} / {n} = {d}')\#
#########################
# from fractions import Fraction as F
#
#
# n = int(input())
# lst = [F(1, i)**2 for i in range(1, n + 1)]
# print(sum(lst))
############
#  Тут и математика особо не нужна. Сумма числителя(верхнее число)
#  и знаменателя(нижнее) в сумме должна быть равна в ведёному числу,
#  при этом числитель должен быть меньше знаменателя,
#  а так же у этой дроби не должна быть альтернатива,
#  т.е. она не должна сокращаться(допустим 2/4 это тоже самое
#  что и 1/2. Получается 2/4 сокращается и она не подходит,
#  а вот 2/3 нельзя сократить, поэтому - подходит)
from fractions import Fraction as F
from math import *
#
#
# n = int(input())
# a = n//2
# b = n-a
#
# def nod(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# while nod(a ,b) != 1:
#     a -= 1
#     b += 1
# print(f'{a}/{b}')
# ###########
# from fractions import Fraction as F
#
#
# fracs = set()
# for i in range(1, int(input()) + 1):
#     for j in range(1, i):
#         fracs.add(F(j, i))
# print(*sorted(fracs), sep='\n')
#############Complex
# a, b = complex(input()), complex(input())
# print(f'{a} + {b} = {a+b}')
# print(f'{a} - {b} = {a-b}')
# print(f'{a} * {b} = {a*b}')
# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j,
#            -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j,
#            -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# res = []
# for i in numbers:
#     res.append(abs(i))
# indexx = res.index(max(res))
# print(numbers[indexx], max(res), sep='\n')
a, b, c = int(input()), complex(input()), complex(input())
z1 = b.conjugate()
z2 = c.conjugate()
print(b**a + c**a + z1**a + z2**(a+1))

