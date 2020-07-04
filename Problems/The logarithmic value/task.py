import math

first = int(input())
second = int(input())

if second <= 0 or second == 1:
    second = math.e

print(round(math.log(first, second), 2))
