# объявление функции
def convert_to_python_case(text):
    result = ''
    for i in text:
        if i.isupper():
            result += '_' + i.lower()
        else:
            if i.upper():
                result += i
    return result[1:].lower()
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))