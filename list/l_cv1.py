numbers = input().split()
print(*sorted(numbers, key=int))
print(*sorted(numbers, reverse=True, key=int))