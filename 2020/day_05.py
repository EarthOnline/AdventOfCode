INPUT = open("./input_files/input_05", "r").read().strip("\n")

PASSES = INPUT.split('\n')


def get_row(spec) -> int:
    seats = range(128)
    for c in spec[:7]:
        seats = seats[:len(seats) // 2] if c == 'F' else seats[len(seats) // 2:]
    return seats[0]


def get_column(spec) -> int:
    seats = range(8)
    for c in spec[-3:]:
        seats = seats[:len(seats) // 2] if c == 'L' else seats[len(seats) // 2:]
    return seats[0]


def get_id(spec) -> int:
    return get_row(spec) * 8 + get_column(spec)


def run_1():
    return max(get_id(x) for x in PASSES)


def run_2():
    ids = [get_id(x) for x in PASSES]
    return [s for s in range(128 * 8) if s not in ids and s - 1 in ids and s + 1 in ids][0]


print(run_1())
print(run_2())
