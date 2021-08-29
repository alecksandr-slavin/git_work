x = int(input())
n = 0

while x != 0:
    digit = x % 10
    x = x // 10
    n = n * 10
    n = n + digit
    print(digit)