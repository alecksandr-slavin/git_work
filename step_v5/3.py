n = int(input())
summ = count = 0
mult = 1
n_last = n % 10
while n != 0:
  count +=1
  num = n % 10
  summ += num
  mult *= num
  n_1 = n
  n //= 10
print(summ, count, mult, summ/count, n_1, n_last + n_1, sep='\n')