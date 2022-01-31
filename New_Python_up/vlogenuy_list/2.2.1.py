num = int(input())
I, II, III, IV = 0, 0, 0, 0
for i in range(num):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        I += 1
    elif x < 0 and y > 0:
        II += 1
    elif x < 0 and y < 0:
        III += 1
    elif x > 0 and y < 0:
        IV += 1

print(f'Первая четверть: {I} \n'
      f'Вторая четверть: {II} \n'
      f'Третья четверть: {III} \n'
      f'Четвертая четверть: {IV} \n')