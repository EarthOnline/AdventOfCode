INPUT = "347991"


def get_coordinate(index):
    ring = 0
    while True:
        side_size = 1 + ring * 2
        grid_size = side_size * side_size
        if grid_size >= index:
            position = grid_size - index
            side = position // (side_size - 1)
            position_on_side = position % (side_size - 1)
            x = 0
            y = 0
            if side == 0:
                x = (side_size - 1) // 2 - position_on_side
                y = ring
            if side == 1:
                x = 0 - ring
                y = (side_size - 1) // 2 - position_on_side
            if side == 2:
                x = 0 - ((side_size - 1) // 2 - position_on_side)
                y = 0 - ring
            if side == 3:
                x = ring
                y = 0 - ((side_size - 1) // 2 - position_on_side)
            return x, y
        ring += 1


def get_adjacent_cells(x, y):
    return [(x - 1, y - 1),
            (x,     y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x,     y + 1),
            (x + 1, y + 1)]


def run_1():
    index = int(INPUT)
    x, y = get_coordinate(index)
    return abs(x) + abs(y)


def run_2():
    number = int(INPUT)
    values = {(0, 0): 1}
    index = 1
    while True:
        index += 1
        x, y = get_coordinate(index)

        value_list = [values.get(l, 0) for l in get_adjacent_cells(x, y)]
        value = sum(value_list)

        if value > number:
            return value
        values[(x, y)] = value


print(run_1())
print(run_2())
