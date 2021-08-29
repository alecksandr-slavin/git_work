n = int(input())

if n % 2 != 0:
    print("YES")
elif n <= 5:
    if n % 2 == 0:
        print("NO")
elif n <= 20:
    if n % 2 == 0:
        print("YES")
elif n > 20 % 2 == 0:
    print("NO")
