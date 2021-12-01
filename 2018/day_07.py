import string
from collections import defaultdict
from typing import Dict, List, Optional

INPUT = open("./input_files/input_07", "r").read().strip("\n")


ALPHABET = string.ascii_uppercase


def build_instuctions() -> Dict[str, List[str]]:
    instructions = defaultdict(list)

    for line in INPUT.split("\n"):
        _, required, _, _, _, _, _, step, _, _ = line.split(" ")
        instructions[step].append(required)
        instructions[required] = instructions[required]
    return instructions


INSTRUCTIONS = build_instuctions()


def get_instruction(finished_instructions: List[str], active_instructions: List[str]) -> Optional[str]:
    valid_instructions = [k for k, v in INSTRUCTIONS.items() if k not in finished_instructions
                          and k not in active_instructions
                          and len(set(v).difference(finished_instructions)) == 0]
    return sorted(valid_instructions)[0] if len(valid_instructions) > 0 else None


def run_1():
    finished_instructions = list()
    while len(finished_instructions) < len(INSTRUCTIONS):
        finished_instructions.append(get_instruction(finished_instructions, list()))
    return "".join(finished_instructions)


def run_2():
    time = -1
    workers = {x: (None, 0) for x in range(5)}
    finished_instructions = list()
    working_instructions = list()
    while len(finished_instructions) < len(INSTRUCTIONS):
        update_workers = dict()
        time += 1
        for worker, (instruction, seconds) in workers.items():
            if instruction is not None:
                if seconds - 1 == 0:
                    finished_instructions.append(instruction)
                    instruction = None
                seconds -= 1
                update_workers[worker] = (instruction, seconds)
        workers.update(update_workers)

        update_workers = dict()
        for worker, (instruction, seconds) in workers.items():
            if instruction is None:
                instruction = get_instruction(finished_instructions, working_instructions)
                if instruction is not None:
                    working_instructions.append(instruction)
                    update_workers[worker] = (instruction, ALPHABET.index(instruction) + 61)
        workers.update(update_workers)
    return time


print(run_1())
print(run_2())
