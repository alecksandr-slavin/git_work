# объявление функции
def is_correct_bracket(text):
    total = 0
    for i in text:
        if '(' in i:
            total += 1
        if ')' in i:
            total -= 1
        if total < 0:
            return False
    if total == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))