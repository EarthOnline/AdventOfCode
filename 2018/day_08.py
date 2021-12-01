from typing import List, Tuple

INPUT = open("./input_files/input_08", "r").read().strip("\n")


LICENSE = list(map(int, INPUT.split(" ")))


def break_children(input: List[int]) -> Tuple[List[int], List[int], int]:
    metadata = list()
    children = list()
    child_count = input[0]
    metadata_count = input[1]
    rest_input = input[2:]
    while len(children) < child_count:
        rest_input, child_metadata, score = break_children(rest_input)
        children.append(score)
        metadata.extend(child_metadata)
    metadata.extend(rest_input[:metadata_count])
    print(children, rest_input[:metadata_count])
    if len(children) == 0:
        score = sum(metadata)
    else:
        score = sum([0 if x > len(children) else children[x-1] for x in rest_input[:metadata_count]])

    return rest_input[metadata_count:], metadata, score


def run_1():
    _, metadata, _ = break_children(LICENSE)
    return sum(metadata)


def run_2():
    _, _, score = break_children(LICENSE)
    return score


print(run_1())
print(run_2())
