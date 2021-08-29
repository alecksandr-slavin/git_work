n = 192

while n > 9:
    summ = 0
    while n > 0:
        last_digit = n % 10
        summ += last_digit
        n = n // 10
    n = summ
print(n)