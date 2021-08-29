from functools import reduce


squares = map(lambda x: x * x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])

print(squares, should, evens)


squaress = [x * x for x in [1, 2, 3, 4, 5]]
shouldd = all([True, True, False])
evenss = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]

print(squaress, shouldd, evenss)