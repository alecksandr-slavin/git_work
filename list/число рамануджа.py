for a in range(1, 41):
    for c in range(1, a):
        for d in range(1, c+1):
            for b in range(1, d):
                if a**3 + b**3 == d**3 + c**3:
                    print(a**3+b**3)