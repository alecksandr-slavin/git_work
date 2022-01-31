from random import *


R = int(input())
result = []
for i in range(R):
    result.append(input())

cop = result[:]
shuffle(cop)

point = 0
while point != R:
    for i in range(R):
        if cop[i] == result[i]:
            shuffle(cop)
            point = 0
        else:
            point += 1

for a in range(len(result)):
    print(f"{result[a]} - {cop[a]}")