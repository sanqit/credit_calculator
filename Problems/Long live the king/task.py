column = int(input())
row = int(input())

can_right = column > 1
can_left = column < 8

can_up = row < 8
can_down = row > 1

moves = 0

if can_up:
    moves += 1
    if can_right:
        moves += 1
    if can_left:
        moves += 1

if can_down:
    moves += 1
    if can_right:
        moves += 1
    if can_left:
        moves += 1

if can_right:
    moves += 1

if can_left:
    moves += 1

print(moves)
