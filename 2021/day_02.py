INPUT = open("./input_files/input_02", "r").read().strip("\n")
# INPUT = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""
INSTRUCTIONS = [tuple(c if i % 2 == 0 else int(c) for i, c in enumerate(x.split(" "))) for x in INPUT.split("\n")]


MACHINE = {
    'forward': lambda f, d, x: (f + x, d),
    'down': lambda f, d, x: (f, d + x),
    'up': lambda f, d, x: (f, d - x)
}

AIM = {
    'forward': lambda a, f, d, x: (a, f + x, d + x * a),
    'down': lambda a, f, d, x: (a + x, f, d),
    'up': lambda a, f, d, x: (a - x, f, d)
}


def run_1():
    f = 0
    d = 0

    for i in INSTRUCTIONS:
        f, d = MACHINE[i[0]](f, d, i[1])
    return f * d


def run_2():
    a = 0
    f = 0
    d = 0

    for i in INSTRUCTIONS:
        a, f, d = AIM[i[0]](a, f, d, i[1])
    return f * d


print(run_1())
print(run_2())
