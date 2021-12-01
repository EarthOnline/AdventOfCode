from collections import defaultdict
from typing import List, Optional


INPUT = open("./input_files/input_07", "r").read().strip("\n")


def run_1():
    definitions = INPUT.split("\n")
    names = set()
    subnames = set()

    for definition in definitions:
        parts = definition.split(' ')
        names.add(parts[0])
        subnames.update([x.replace(',', '') for x in parts[3:]])

    return [x for x in names if x not in subnames][0]


class Program:
    __instances = dict()

    @staticmethod
    def get_instance(name: str):
        if name in Program.__instances:
            return Program.__instances[name]
        return Program(name)

    name: str
    weight: Optional[int]
    children: List

    def __init__(self, name: str):
        self.name = name
        self.weight = None
        self.children = list()

        Program.__instances[name] = self

    def get_weight(self):
        return self.weight + sum([x.get_weight() for x in self.children])

    def is_balanced(self):
        weights = [x.get_weight() for x in self.children]
        return min(weights) == max(weights)

    def find_imbalance(self, diff=None):
        weights = defaultdict(int)
        for child in self.children:
            weights[child.get_weight()] += 1

        if diff is None and len(weights) > 1 and len(self.children) > 2:
            real_value = 0
            bad_value = 0
            for weight, count in weights.items():
                if count == 1:
                    bad_value = weight
                else:
                    real_value = weight
            diff = real_value - bad_value

        for child in self.children:
            if not child.is_balanced():
                return child.find_imbalance(diff=diff)
            if weights[child.get_weight()] == 1:
                return child.find_imbalance(diff=diff)
        return self.weight + diff


def run_2():
    definitions = INPUT.split("\n")

    for definition in definitions:
        parts = definition.split(' ')
        program = Program.get_instance(parts[0])
        program.weight = int(parts[1][1:-1])
        program.children.extend([Program.get_instance(x.replace(',', '')) for x in parts[3:]])

    return Program.get_instance(run_1()).find_imbalance()


print(run_1())
print(run_2())
