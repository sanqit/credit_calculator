a = int(input())
b = int(input())

mod3 = []
for number in range(a, b + 1):
    if number % 3 == 0:
        mod3.append(number)

print(sum(mod3) / len(mod3))
