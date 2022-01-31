import random
#
# n = int(input())    # количество попыток
# coin = {1: 'Решка', 2: 'Орел'}
# for i in range(n):
#     num = random.randint(1, 2)
#     print(coin[num])
###########
#
# n = int(input())    # количество попыток
# print(*[random.randint(1, 6) for _ in range(n)], sep='\n')
import random

result = []
while len(result) != 7:
    x = random.randint(1, 49)
    if x not in result:
        result.append(x)
print(*result)