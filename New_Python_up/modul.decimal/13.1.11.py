from decimal import *
num = Decimal(input())

num_as = num.as_tuple()
if int(num) == 0:
    print(max(num_as.digits))
else:
    print(sum((max(num_as.digits), min(num_as.digits))))
