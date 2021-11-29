def is_palindrome(text):
    spisok = ''
    for i in text:
        if i.isalpha() or i.isdigit():
            spisok += i

    if spisok == spisok[::-1]:
        return True
    else:
        return False


def is_prime(num):
    numbs = int(num)
    return len([i for i in range(1, numbs+1) if numbs % i == 0]) == 2


# объявление функции
def is_valid_password(password):
    a, b, c = password[0], int(password[1]), int(password[2])
    if len(password) == 3:
        if is_palindrome(a):
            if is_prime(b):
                if int(c) % 2 == 0:
                    return True
    return False


psw = input().split(':')

# вызываем функцию
print(is_valid_password(psw))
