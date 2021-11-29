# объявление функции
def get_days(month):
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return mon[month - 1]
# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))