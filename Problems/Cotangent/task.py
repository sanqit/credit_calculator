import math

deg = int(input())
rad = math.radians(deg)

ctg = 1 / math.tan(rad)

print(round(ctg, 10))
