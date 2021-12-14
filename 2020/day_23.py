INPUT = open("./input_files/input_23", "r").read().strip("\n")
# INPUT = """389125467"""
CUPS = [int(x) for x in INPUT]


def move(cups):
    pick_up = cups[1:4]
    cups = cups[:1] + cups[4:]
    options = [x for x in cups if x < cups[0]]
    destination = cups.index(max(options) if len(options) > 0 else max(cups))
    return cups[1:destination + 1] + pick_up + cups[destination + 1:] + cups[:1]


def run_1():
    cups = CUPS
    for _ in range(100):
        cups = move(cups)

    destination = cups.index(1)
    return ''.join(str(x) for x in cups[destination + 1:] + cups[0:destination])


def run_2():
    return


print(run_1())
print(run_2())
