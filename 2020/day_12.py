INPUT = open("./input_files/input_12", "r").read().strip("\n")

INSTRUCTIONS = [(i[0], int(i[1:])) for i in INPUT.split('\n')]

MAPPING = {
    0: 'E',
    90: 'S',
    180: 'W',
    270: 'N'
}

ACTIONS = dict(  # x_coord, y_coord, facing, input
    N=lambda x, y, f, i: (x, y + i, f),
    E=lambda x, y, f, i: (x + i, y, f),
    S=lambda x, y, f, i: (x, y - i, f),
    W=lambda x, y, f, i: (x - i, y, f),
    L=lambda x, y, f, i: (x, y, (f - i) % 360),
    R=lambda x, y, f, i: (x, y, (f + i) % 360),
    F=lambda x, y, f, i: ACTIONS[MAPPING.get(f)](x, y, f, i)
)


def run_1():
    x = y = f = 0
    for action, input in INSTRUCTIONS:
        x, y, f = ACTIONS[action](x, y, f, input)
    return abs(x) + abs(y)


def rotate(x, y, deg):
    if deg in [90, 270]:
        _y = y
        y = 0 - x
        x = _y

    if deg in [180, 270]:
        x = 0 - x
        y = 0 - y

    return x, y


ACTIONS2 = dict(  # ship x_coord, ship y_coord, waypoint x_coord, waypoint y_coord, input
    N=lambda sx, sy, wx, wy, i: (sx, sy, wx, wy + i),
    E=lambda sx, sy, wx, wy, i: (sx, sy, wx + i, wy),
    S=lambda sx, sy, wx, wy, i: (sx, sy, wx, wy - i),
    W=lambda sx, sy, wx, wy, i: (sx, sy, wx - i, wy),
    L=lambda sx, sy, wx, wy, i: (sx, sy, *rotate(wx, wy, 360 - i)),
    R=lambda sx, sy, wx, wy, i: (sx, sy, *rotate(wx, wy, i)),
    F=lambda sx, sy, wx, wy, i: (sx + wx * i, sy + wy * i, wx, wy)
)


def run_2():
    sx = sy = 0
    wx = 10
    wy = 1
    for action, input in INSTRUCTIONS:
        sx, sy, wx, wy = ACTIONS2[action](sx, sy, wx, wy, input)
    return abs(sx) + abs(sy)


print(run_1())
print(run_2())
