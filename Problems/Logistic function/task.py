import math

def sigmoid(x):
    return 1 / (1 + math.pow(math.e, -x))

value = int(input())

print(round(sigmoid(value), 2))
