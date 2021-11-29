def is_valid(n):
    if n.isdigit() and 1 < int(n) < 100:
        return True
    else:
        return False


def is_valid_num():
    while True:
        num = input()
        if is_valid(num) == True:
            n = int(num)
            break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

