n = int(input())

numbers = []
for _ in range(n):
    number = int(input())
    if number % 7 == 0:
        numbers.append(number)

for number in numbers:
    print(number ** 2)
