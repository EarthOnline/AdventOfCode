from copy import copy, deepcopy
from functools import reduce
from operator import mul, add
from typing import List

INPUT = open("./input_files/input_11", "r").read().strip("\n")


class Monkey:
    @staticmethod
    def read_input(text):
        result = {}
        text_input = [x.strip() for x in text.split('\n')]
        result['starting_items'] = [int(x) for x in text_input[1].split(':')[1].strip().split(', ')]

        op_input, val_input = text_input[2].split(' ')[-2:]
        op = mul if op_input == '*' else add
        result['operation'] = lambda x: op(x, x if val_input == 'old' else int(val_input))

        result['test_value'] = int(text_input[3].split(' ')[-1])
        result['target_1'] = int(text_input[4].split(' ')[-1])
        result['target_2'] = int(text_input[5].split(' ')[-1])
        return result

    def test(self, item):
        return item % self.test_value == 0

    def __init__(self, starting_items, operation, test_value, target_1, target_2):
        self.items = starting_items
        self.operation = operation
        self.test_value = test_value
        self.target_1 = target_1
        self.target_2 = target_2

        self.inspectiont_count = 0

    def round(self, monkeys, anxiety_management):
        items = copy(self.items)
        self.items = []
        for item in items:
            self.inspectiont_count += 1
            item = self.operation(item)
            item //= anxiety_management
            item %= reduce(mul, [m.test_value for m in monkeys])
            monkeys[self.target_1 if self.test(item) else self.target_2].items.append(item)


MONKEYS = [Monkey(**Monkey.read_input(x)) for x in INPUT.split('\n\n')]


def play_round(monkeys, anxiety_management=1):
    for monkey in monkeys:
        monkey.round(monkeys, anxiety_management)


def calculate_score(monkeys: List[Monkey]) -> int:
    return reduce(mul, sorted(m.inspectiont_count for m in monkeys)[-2:])


def run_1():
    monkeys = deepcopy(MONKEYS)
    for _ in range(20):
        play_round(monkeys, 3)
    return calculate_score(monkeys)


def run_2():
    monkeys = deepcopy(MONKEYS)
    for _ in range(10000):
        play_round(monkeys)
    return calculate_score(monkeys)


print(run_1())
print(run_2())
