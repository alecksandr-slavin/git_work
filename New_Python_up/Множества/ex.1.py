# n, m, k, p = [int(input()) for _ in range(4)]
# print(n - ((m + k) - p))
##############
#2
# ls = input().split()
# a = set(ls)
# print(len(ls) - len(a))
# res = set()
# for i in range(int(input())):
#     res.add(input())
# f = input()
# if f in res:
#     print('REPEAT')
# else:
#     print('OK')
################
# m = int(input())
# n = int(input())
# dom = {input() for _ in range(m)}
# for i in range(n):
#     if input() in dom:
#         print('YES')
#     else:
#         print('NO')
#############
# a = {int(i) for i in input().split()}
# b = {int(i) for i in input().split()}
# res = set(a.intersection(b))
# if len(res) == 0:
#     print('BAD DAY')
# else:
#     print(*sorted(res, reverse=True))
# myset1 = {int(i) for i in input().split()}
# myset2 = {int(i) for i in input().split()}
#
# f = myset2 - myset1
# flag = myset1.issubset(myset2)
# if len(f) != 0:
# #     print('NO')
# # else:
# #     if flag == True:
# #         print('YES')
# #     else:
# #         print('NO')
# m, n = int(input()), int(input())
# mat = {input() for _ in range(m)}
# info = {input() for _ in range(n)}
#
# res = set()
# res.update(mat - info)
# res.update(info - mat)
#
# if len(res) == 0:
#     print('NO')
# else:
#     print(len(res))
###########
# a, b = set(input().split()), set(input().split())
# a.update(b)
# print(*sorted(a))

#############
# m = int(input())
# n = int(input())
# all_shool = [input()  for _ in range(m+n)]
#
# a = {}
# for i in all_shool:
#     a.setdefault(i, all_shool.count(i))
#
# couny = 0
# for i in a.values():
#     if i == 1:
#         couny += 1
# if couny == 0:
#     print('NO')
# else:
#     print(couny)
# #########
# # res = [input() for _ in range(int(input()))]
# one = set(res[0])
# for i in res:
# #     one.intersection_update(i)
# # print(*sorted(one))
res = [{input() for _ in range(int(input()))} for _ in range(int(input()))]
one = set(res[0])
for i in res:
    one.intersection_update(i)
print(sorted(one), sep='\n')

