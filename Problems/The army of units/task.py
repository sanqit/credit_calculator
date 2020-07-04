units_count = int(input())

if units_count < 1:
    print("no army")
elif units_count < 10:
    print("few")
elif units_count < 50:
    print("pack")
elif units_count < 500:
    print("horde")
elif units_count < 1000:
    print("swarm")
else:
    print("legion")
