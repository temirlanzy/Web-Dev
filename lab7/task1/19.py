import math

x = int(input())
count = 0

for d in range(1, int(math.sqrt(x)) + 1):
    if x % d == 0:
        count += 1
        if d != x // d:
            count += 1

print(count)
