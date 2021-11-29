# объявление функции
def find_all(target, symbol):
    rezult = []
    rezult.extend(target)
    total = []
    for i in range(0, len(rezult)):
        if rezult[i] == symbol:
            total.append(i)
    return total
# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))