# объявление функции
def is_prime(nu):
    return len([i for i in range(1, nu+1) if nu % i == 0]) == 2


# объявление функции
def get_next_prime(num):
    while True:
        if is_prime(num + 1) == False:
            num = num + 1
            continue
        return num + 1

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))