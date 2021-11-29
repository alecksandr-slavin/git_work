def vse_i_srazu(sp):
    shag = 1
    result = [[]]
    while shag <= len(result):
        for i in range(0, len(sp) + 1):
            result.append(sp[i:i + shag])
        shag += 1
    return result


stroka = input().split()
print(vse_i_srazu(stroka))
