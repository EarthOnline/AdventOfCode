from time import time

start = time()
INPUT = open("./input_files/input_25", "r").read().strip("\n")

TRANSLATE = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '='
}


def from_snafu(value):
    result = 0
    for index, digit in enumerate(value[::-1]):
        base = 5 ** index
        result += base * TRANSLATE[digit]
    return result


def to_snafu(value):
    result = []
    power = 0
    while value != value % (5 ** power):
        power += 1

    power -= 1
    while power >= 0:
        base = 5 ** power
        change = value // base

        result.append(change)
        value -= change * base
        power -= 1

    for i, _ in enumerate(result[::-1], start=1):
        v = result[0 - i]
        if v < -2:
            result[0 - i] += 5
            result[0 - i - 1] -= 1
        if v > 2:
            result[0 - i] -= 5
            result[0 - i - 1] += 1
    return ''.join(TRANSLATE[x] for x in result)


BURNERS = [from_snafu(x) for x in INPUT.split('\n')]


def run_1():
    return to_snafu(sum(BURNERS))


def run_2():
    return "* * * Merry Christmas * * *"


print('\n', 'Part 1 ==> ', run_1())
print(f'in {int((time() - start) * 1000)} ms')
print('\n', 'Part 2 ==> ', run_2())
print(f'in {int((time() - start) * 1000)} ms')
