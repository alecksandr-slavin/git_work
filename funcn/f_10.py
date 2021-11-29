# объявление функции
def is_password_good(password):
    numbs = "0123456789"
    f1 = f2 = f3 = False

    if len(password) < 8:
        return False

    for i in password:
        if i.isupper():
            f1 = True

        elif i.islower():
            f2 = True

        elif i in numbs:
            f3 = True

    if f1 * f2 * f3:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
