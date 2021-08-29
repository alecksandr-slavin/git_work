total = 0
for a in range(0, 100):
    for b in range(0, 100):
        for c in range(0, 100):
            if (10 * a + 5 * b + 0.5 * c == 100) and (a + b + c == 100):
                print('x =', a, 'y =', b, 'z =', c)