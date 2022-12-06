INPUT = open("./input_files/input_01", "r").read().strip("\n")

MOVES = [(x[0], int(x[1:])) for x in INPUT.split(', ')]


def move(f, x, y, step):
    match step[0]:
        case 'R':
            f += 1
        case 'L':
            f -= 1
    f = f % 4

    match f:
        case 0:
            action = lambda _x, _y: (_x, _y + 1)
        case 1:
            action = lambda _x, _y: (_x + 1, _y)
        case 2:
            action = lambda _x, _y: (_x, _y - 1)
        case 3:
            action = lambda _x, _y: (_x - 1, _y)
        case _:
            action = lambda _x, _y: (_x, _y)

    visited = []
    for _ in range(step[1]):
        x, y = action(x, y)
        visited.append((x, y))
    return f, x, y, visited


def run_1():
    f = x = y = 0
    for step in MOVES:
        f, x, y, _ = move(f, x, y, step)
    return abs(x) + abs(y)


def run_2():
    positions = {(0, 0), }
    f = x = y = 0
    for step in MOVES:
        positions.add((x, y))
        f, x, y, visited = move(f, x, y, step)
        twice = [v for v in visited if v in positions]
        if twice:
            x, y = twice[0]
            return abs(x) + abs(y)
        positions.update(visited)
    return


print(run_1())
print(run_2())
