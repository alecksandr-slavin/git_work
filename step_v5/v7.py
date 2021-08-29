n = int(input())
while n != 0:
    a = n % 10
    n //= 10
    b = n % 10
    n //= 10
if a < b:
    print("YES")
else:
    print("NO")