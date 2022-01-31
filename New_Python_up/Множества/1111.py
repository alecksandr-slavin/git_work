# it = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45,
#          '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# print(*sorted({int(i) for i in it}))
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime',
#          'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# res = {i[0].lower() for i in words}
# print(*sorted(res))
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#  pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
#   you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#    those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#     traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# res = {i.strip(".,()'':;!?") for i in sentence.lower().split() if len(i) == 4}
# print(*sorted(res))
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for
#  a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which,
#   if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#    those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#     traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# res = {i.strip(".,()'':;!?") for i in sentence.lower().split() if len(i.strip(".,()'':;!?")) < 4}
# print(*sorted(res))

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py',
         'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt',
         'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

res = {i.strip("''").lower() for i in files if i[-4:].lower() == '.png'}
print(*sorted(res))

    