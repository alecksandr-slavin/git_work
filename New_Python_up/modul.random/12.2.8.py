from random import *

res = set()
while len(res) != 100:
    res.add(randint(1000000, 9000000))
print(*res, sep='\n')
