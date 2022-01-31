d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
ls = input().strip('"').upper()
for s in ls:
    for a, b in d.items():
        if s in b:
            print(((b.index(s)+1) * a), end='')
