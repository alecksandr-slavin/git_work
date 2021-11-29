# for i in input().split():
#     print('.'.join(i[0][0]), end='.')

#############

#
# s = n.split("\\")
# print('\n'.join(s))
n = input().split('.')
flag = ''
for i in n:
    if int(i) > 255:
        flag = 'НЕТ'
        break
    else:
        flag = 'ДА'
print(flag)

