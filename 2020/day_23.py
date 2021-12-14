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


def get_destination(pick_up, selected):
    dest = selected.marking
    while True:
        dest -= 1
        if dest < 1:
            dest = 1000000 - dest
        if dest not in pick_up:
            return dest


class ChainedCup:
    def __init__(self, marking: int, prev):
        self.marking = marking
        self.next = None
        if prev:
            prev.next = self

    def get_next(self, count):
        if count == 0:
            return self.next
        return self.next.get_next(count-1)

    def get_values(self, count):
        if count == 1:
            return [self.marking]
        return [self.marking] + self.next.get_values(count - 1)


def build_chain():
    quick_search = {}
    selected = None
    last = None

    for r in range(1000000):
        marking = CUPS[r] if r < len(CUPS) else r + 1
        last = ChainedCup(marking, last)
        if selected is None:
            selected = last
        quick_search[marking] = last
    last.next = selected
    return selected, quick_search


def run_2():
    selected, quick_search = build_chain()
    for _ in range(10000000):
        pickup = selected.next
        selected.next = selected.get_next(3)
        dest = quick_search[get_destination(pickup.get_values(3), selected)]
        end = dest.next
        dest.next = pickup
        pickup.get_next(1).next = end
        selected = selected.next
    cups = quick_search[1].next.get_values(2)
    return cups[0] * cups[1]


print(run_1())
print(run_2())
