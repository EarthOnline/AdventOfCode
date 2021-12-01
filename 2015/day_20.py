import math
from typing import List

INPUT = 33100000
INPUT = 29000000


def get_divisors(number: int) -> List[int]:
    large_divisors = []
    for x in range(1, int(math.sqrt(number) + 1)):
        if number % x == 0:
            yield x
            if x*x != number:
                large_divisors.append(number // x)
    for divisor in reversed(large_divisors):
        yield divisor


def run_1():
    target = INPUT // 10
    house = 0
    while True:
        house += 1
        if target == sum(get_divisors(house)):
            break
    return house


print(run_1())
