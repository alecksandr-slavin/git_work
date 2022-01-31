# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# point = 1
# for i in range(len(numbers)):
#     num = numbers[i] * point
#     point = num
# print(point)
#
# data = 'Python для продвинутых!'
# res = tuple(data)
# print(res)
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
res = list(poet_data)
res[-1] = 'Москва'
print(tuple(res))