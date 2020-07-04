score = int(input())
top = int(input())

percent = score / top

if percent < .60:
    print("F")
elif percent < .70:
    print("D")
elif percent < .80:
    print("C")
elif percent < .90:
    print("B")
else:
    print("A")
