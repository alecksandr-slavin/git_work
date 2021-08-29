text = int(input())
total = 0
while text != 0:
    if text >= 25:
        total += 1
        text -= 25
    elif text >= 10:
        total += 1
        text -= 10
    elif text >= 5:
        total += 1
        text -= 5
    elif text >= 1:
        total += 1
        text -= 1
print(total)