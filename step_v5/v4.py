text = int(input())
total = 0
while text <= 5 and text > -1:
    if text == 5:
        total += 1
    text = int(input())
print(total)