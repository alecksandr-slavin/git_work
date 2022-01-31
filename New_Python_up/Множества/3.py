# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# a = sorted(fruits, reverse=True)
# print(*a, sep='\n')
#################
# print(len(set(input())))
num = input()
if len(num) == len(set(num)):
    print("YES")
else:
    print('NO')
