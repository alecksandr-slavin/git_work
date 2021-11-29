from random import *


def get_minimal_way(right):
    left = 1
    num = randint(left, right)
    num = num // 2 + num % 2
    count = 1
    while count < 100:
        middle = (left + right) // 2
        if middle > num:
            left = middle + 1
            count += 1
            continue
        if middle < num:
            right = middle - 1
            count += 1
            continue
        if middle == num:
            break
    print(count)


get_minimal_way(int(input()))