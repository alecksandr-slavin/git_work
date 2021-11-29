# объявление функции
def is_palindrome(text):
    spisok = ''
    for i in text:
        if i.isalpha() or i.isdigit():
            spisok += i

    return spisok == spisok[::-1]

# считываем данные
txt = input().upper()

# вызываем функцию
print(is_palindrome(txt))
