# a = int(input())
# while a % 7 == 0:
#     print(a)
#     a = int(input())

text = int(input())
total = 0
while text > 0:
    num = int(text)
    total += num
    text = int(input())
print(total)