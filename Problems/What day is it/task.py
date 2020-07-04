offset = int(input())

time = 10.5
n = time + offset
if n < 0:
    print("Monday")
elif n > 24:
    print("Wednesday")
else:
    print("Tuesday")
