first = float(input())
second = float(input())
op = input()

if second == 0 and op in ("/", "mod", "div"):
    out = "Division by 0!"
elif op == "+":
    out = first + second
elif op == "-":
    out = first - second
elif op == "/":
    out = first / second
elif op == "*":
    out = first * second
elif op == "mod":
    out = first % second
elif op == "pow":
    out = first ** second
elif op == "div":
    out = first // second

print(out)
