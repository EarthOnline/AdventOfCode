from itertools import chain
from json import loads
from operator import mul

INPUT = open("./input_files/input_13", "r").read().strip("\n")

PAIRS = [[loads(y) for y in x.split('\n')] for x in INPUT.split('\n\n')]


def check(pair):
    left, right = pair
    left_type, right_type = [type(p) for p in pair]

    if left_type == right_type == int:
        return None if left == right else left < right
    if left_type == right_type == list:
        results = [r for r in map(check, zip(left, right)) if r is not None]
        if results:
            return results[0]

        left_len, right_len = [len(p) for p in pair]
        return None if left_len == right_len else left_len < right_len
    return check(([left] if left_type == int else left,
                  [right] if right_type == int else right))


def run_1():
    return sum(i for i, p in enumerate(PAIRS, start=1) if check(p))


def run_2():
    packets = list(chain.from_iterable(PAIRS))
    dividers = [[[2]], [[6]]]

    ordered_packets = []
    for packet in packets + dividers:
        for i, op in enumerate(ordered_packets):
            if not check((op, packet)):
                ordered_packets.insert(i, packet)
                break
        else:
            ordered_packets.append(packet)

    return mul(*[i for i, v in enumerate(ordered_packets, start=1) if v in dividers])


print(run_1())
print(run_2())
