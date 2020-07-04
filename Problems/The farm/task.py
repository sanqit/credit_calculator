chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

total = int(input())


def print_result(price, singular, plural):
    count = total // price
    if count > 0:
        word = singular if count == 1 else plural
        print(str(count) + " " + word)
        return True
    return False


if not(print_result(sheep_price, "sheep", "sheep") or print_result(cow_price, "cow", "cows") or print_result(pig_price, "pig", "pigs") or print_result(goat_price, "goat", "goats") or print_result(chicken_price, "chicken", "chickens")):
    print("None")
