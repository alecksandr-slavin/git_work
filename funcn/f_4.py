# объявление функции
def number_of_factors(num):
    rezult = [i for i in range(1, num + 1) if num % i == 0]
    return len(rezult)

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))