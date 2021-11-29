
from math import *

right = int(input())
right = right - 1
total = 1
left = 1
while total < 100:
    middle = ceil((left + right) // 2)
    if middle < right:
        left = middle + 1
        total += 1
        continue
    if middle > right:
        right = middle - 1
        total += 1
        continue
    if middle == right:
        break
print(total)


# Называем число, равное middle = (left + right) // 2;
# Если число middle равно задуманному числу, то мы угадали!;
# Если число middle меньше задуманного числа, то положим left = middle + 1 и продолжим алгоритм;
# Если число middle больше задуманного числа, то положим right = middle - 1 и продолжим алгоритм.
# Поскольку на каждой итерации мы отбрасываем половину чисел, то гарантировано угадаем задуманное число за величину, равную \log_2 nlog
# 2
# ​
#  n (двоичный логарифм) округленную до целого в большую сторону. При n=100n=100 получаем 77 попыток.