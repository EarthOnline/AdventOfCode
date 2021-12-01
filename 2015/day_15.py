from functools import reduce
from operator import add, mul
from typing import List, Dict, Tuple, Callable

INPUT = open("./input_files/input_15", "r").read().strip("\n")


def get_ingredients() -> Dict[str, Tuple[int, int, int, int, int]]:
    result = dict()
    for ingredient in INPUT.split("\n"):
        parts = ingredient.split(" ")
        result[parts[0][:-1]] = \
            (int(parts[2][:-1]), int(parts[4][:-1]), int(parts[6][:-1]), int(parts[8][:-1]), int(parts[10]))
    return result


INGREDIENTS = get_ingredients()


def recipe_score(amounts: Tuple[int, int, int, int], requirement: Callable[[List[int]], bool]) -> int:
    scores = reduce(lambda x, y: list(map(add, x, y)),
                    [[x * amounts[index] for x in specs] for index, specs in enumerate(INGREDIENTS.values())])
    scores = [x if x > 0 else 0 for x in scores]
    if requirement(scores):
        return reduce(mul, scores[:-1])
    return 0


def get_combinations(size: 100, requirement: Callable[[List[int]], bool] = lambda x: True) -> List[int]:
    result = list()
    for x in range(1, size - 2):
        for y in range(1, size - 1 - x):
            for z in range(1, size - x - y):
                result.append(recipe_score((x, y, z, size - x - y - z), requirement))
    return result


def run_1():
    return max(get_combinations(100))


def run_2():
    return max(get_combinations(100, lambda x: x[4] == 500))


print(run_1())
print(run_2())
