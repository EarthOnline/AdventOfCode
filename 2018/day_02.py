from collections import defaultdict
from typing import Dict, Tuple, List

INPUT = open("./input_files/input_02", "r").read().strip("\n")


BOX_IDS = [x for x in INPUT.split("\n")]


def has_similar(box_id: str, required: int) -> bool:
    letter_dict = defaultdict(int)
    for letter in box_id:
        letter_dict[letter] += 1
    return len([x for x in letter_dict.values() if x == required]) > 0


def get_differences() -> Dict[int, List[Tuple[int, int]]]:
    differences = defaultdict(list)
    for index, box_id in enumerate(BOX_IDS):
        for x in range(index + 1, len(BOX_IDS)):
            diff = [l for i, l in enumerate(box_id) if l != BOX_IDS[x][i]]
            differences[len(diff)].append((index, x))
    return differences


def run_1():
    match_2 = [x for x in BOX_IDS if has_similar(x, 2)]
    match_3 = [x for x in BOX_IDS if has_similar(x, 3)]
    return len(match_2) * len(match_3)


def run_2():
    differences = get_differences()
    box_id_1, box_id_2 = differences[min(differences.keys())][0]
    return "".join([l for i, l in enumerate(BOX_IDS[box_id_1]) if l == BOX_IDS[box_id_2][i]])


print(run_1())
print(run_2())
