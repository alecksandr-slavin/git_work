# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: numbers[i]**2 for i in range(len(numbers))}
##################################
#6
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None,
#           'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink',
#           'c7': 'Orange', 'c8': None, 'c9': 'White',
#           'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold',
#           'c13': None, 'c14': 'Amber', 'c15': 'Azure',
#           'c16': 'Beige', 'c17': 'Bronze', 'c18': None,
#           'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
#           'c22': 'Sand', 'c23': None}
#
# result = {i: colors.get(i) for i, j in colors.items() if j is not None}
# print(result)
######################3
#7
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19,
#                     'roman': 123, 'rebecca': 293, 'ronald': 76,
#                     'dorothy': 62, 'harold': 36, 'matt': 314,
#                     'kim': 451, 'rosaly': 18, 'rustam': 89,
#                     'soltan': 111, 'amir': 654, 'dima': 390,
#                     'amiran': 777, 'geor': 999, 'sveta': 75,
#                     'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if len(str(value)) == 2}
# print(result)
####################
#8
# months = {1: 'January', 2: 'February', 3: 'March',
#           4: 'April', 5: 'May', 6: 'June', 7: 'July',
#           8: 'August', 9: 'September', 10: 'October',
#           11: 'November', 12: 'December'}
#
# result = {value: key for key, value in months.items()}
# print(result)
###########
#9
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain' \
#     ' 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(i[:i.index(':')]): i[i.index(':')+1:] for i in s.split()}
# print(result)
####################
#10
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95,
#            1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {num: [x for x in range(1, num + 1) if num % x == 0] for num in numbers}
# print(result)
#################
#11
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {key: [ord(x) for x in key] for key in words}
# print(result)
####################
#12
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F',
#            6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
#            12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
#            17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V',
#            22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# res = {letters.pop(i) for i in remove_keys}
# result = letters
# print(result)
##################
#13
# students = {'Timur': (170, 75), 'Ruslan': (180, 105),
#             'Soltan': (192, 68), 'Roman': (175, 70),
#             'Madlen': (160, 50), 'Stefani': (165, 70),
#             'Tom': (190, 90), 'Jerry': (180, 87),
#             'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120),
#             'Max': (200, 110), 'Barak': (180, 89),
#             'Donald': (170, 80), 'Rustam': (186, 100),
#             'Alice': (159, 59), 'Rita': (170, 80),
#             'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}
# print(result)
##############3
# #14
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15),
#           (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30),
#           (31, 32, 33), (34, 35, 36)]
#
#
# result = {i[0]: i[1:] for i in tuples if list(i)}
# print(result)
######################
#15
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]
# print(result)
import random

random.seed(18)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))