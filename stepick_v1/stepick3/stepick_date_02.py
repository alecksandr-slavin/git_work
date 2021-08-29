with open('pop_01.txt') as inf:
    a = inf.read().replace('\n', ' ').lower().split()

s = set(a)
counter = 0
word = a[0]
for x in s:
    if counter < a.count(x):
        counter = a.count(x)
        word = x
    if counter == a.count(x):
        if x < word:
            word = x

result = word + ' ' + str(counter)


with open('data_02.txt', 'w') as ouf:
    ouf.write(str(result))
