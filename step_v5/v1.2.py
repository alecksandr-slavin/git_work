n = int(input())

total_sum = 0  #
counter = 0  #
total_comp = 1  #
total_sum_counter = 0  #
first = int(n) // 10
last = first + int(n) % 10

while n > 0:
    digit = n % 10
    total_sum += digit
    total_comp *= digit
    n = n // 10

while n > 0:
    i = n % 10
    n = n / 10
    counter = counter + i

for i in range(1, int(n)+1):
    a = input(str(int(i)))
    total_sum_counter += float(a)
total_sum_counter /= int(n)

print(total_sum, counter, total_comp, total_sum_counter, first, last, sep='\n')