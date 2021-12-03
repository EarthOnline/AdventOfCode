from collections import defaultdict
from typing import List

INPUT = 33100000


def get_divisors(number: int) -> List[int]:
    return [x for x in range(1, number + 1) if number % x == 0]


def run_1():
    houses = [0 for _ in range(INPUT // 10)]

    for i in range(1, INPUT // 10):
        for j in range(i, INPUT // 10, i):
            houses[j] += i * 10

    for i, h in enumerate(houses):
        if h >= INPUT:
            return i


def run_2():
    houses = [0 for _ in range(INPUT // 10)]

    for i in range(1, INPUT // 10):
        for j in range(i, min(INPUT // 10, i * 50), i):
            houses[j] += i * 11

    for i, h in enumerate(houses):
        if h >= INPUT:
            return i


print(run_1())
print(run_2())
