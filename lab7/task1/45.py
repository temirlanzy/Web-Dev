from itertools import product

x, y, z, n = (int(input()) for _ in range(4))

result = [[a, b, c] for a, b, c in product(range(x + 1), range(y + 1), range(z + 1)) if a + b + c != n]

print(result)
