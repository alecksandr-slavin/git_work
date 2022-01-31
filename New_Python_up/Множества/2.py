n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
x1 = m + n - x - t
x2 = n + k - z - t
x3 = m + k - y - t
one_books = (n - x1 - x2 - t) + (m - x1 - t - x3) + (k - x2 - t - x3)
two_books = x1 + x2 + x3
zero_books = a - (one_books + two_books + t)
print(one_books, two_books, zero_books, sep="\n")