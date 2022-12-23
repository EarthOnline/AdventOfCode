import string
from operator import add, sub, mul, floordiv
from time import time

start = time()
INPUT = open("./input_files/input_21", "r").read().strip("\n")

MONKEYS = {m: int(o) if o[0] in string.digits else tuple(o.split(' ')) for m, o in
           [x.split(': ') for x in INPUT.split('\n')]}

OPPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv,
}

NEG_OPPERATORS = {
    '+': sub,
    '-': add,
    '*': floordiv,
    '/': mul,
}

TRANSLATE = {
    '-': '+',
    '/': '*'
}


def yell(monkey):
    result = MONKEYS.get(monkey)
    if type(result) == int:
        return result

    monkey_1, opp, monkey_2 = result
    return OPPERATORS[opp](yell(monkey_1), yell(monkey_2))


def solve(monkey, target):
    if monkey == 'humn':
        return target

    monkey_1, opp, monkey_2 = MONKEYS[monkey]
    try:
        _target = yell(monkey_1)

        _opp = TRANSLATE.get(opp, opp)
        # print(target, '=', _target, opp, abs(NEG_OPPERATORS[_opp](target, _target)))
        result = solve(monkey_2, abs(NEG_OPPERATORS[_opp](target, _target)))
    except TypeError:
        _target = yell(monkey_2)
        # print(target, '=', NEG_OPPERATORS[opp](target, _target), opp, _target)
        result = solve(monkey_1, NEG_OPPERATORS[opp](target, _target))
    return result


def run_1():
    return yell('root')


def run_2():
    monkey_1, opp, monkey_2 = MONKEYS['root']
    MONKEYS.pop('humn')
    try:
        target = yell(monkey_1)
        result = solve(monkey_2, target)
    except TypeError:
        target = yell(monkey_2)
        result = solve(monkey_1, target)

    return result


print('\n', 'Part 1 ==> ', run_1())
print(f'in {int((time() - start) * 1000)} ms')
print('\n', 'Part 2 ==> ', run_2())
print(f'in {int((time() - start) * 1000)} ms')
