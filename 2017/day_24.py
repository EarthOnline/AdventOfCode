from collections import defaultdict
from copy import deepcopy
from typing import Dict, List, Tuple

INPUT = open("./input_files/input_24", "r").read().strip("\n")
# INPUT = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"


def building_blocks(input: str) -> Dict[int, List[Tuple[int, int]]]:
    blocks = [tuple([int(y) for y in x.split("/")]) for x in input.split("\n")]
    result = defaultdict(list)

    for block in blocks:
        result[block[0]].append(block)
        result[block[1]].append(block)
    return result


def remove_block(blocks: Dict[int, List[Tuple[int, int]]], block: Tuple[int, int]
                 ) -> Dict[int, List[Tuple[int, int]]]:
    result = deepcopy(blocks)
    result[block[0]].remove(block)
    result[block[1]].remove(block)
    return result


def build_bridges(blocks: Dict[int, List[Tuple[int, int]]], start: int, prefix: List[Tuple[int, int]]
                  ) -> List[List[Tuple[int, int]]]:
    result = list()
    for block in blocks[start]:
        result.append(prefix + [block])
        end = block[1] if block[0] == start else block[0]
        result.extend(build_bridges(remove_block(blocks, block), end, prefix + [block]))
    return result


def run_1():
    blocks = building_blocks(INPUT)
    bridges = build_bridges(blocks, 0, list())
    print(max([sum([x[0] + x[1] for x in b]) for b in bridges]))
    max_length = max([len(x) for x in bridges])
    long_bridges = [x for x in bridges if len(x) == max_length]
    return max([sum([x[0] + x[1] for x in b]) for b in long_bridges])


print(run_1())
