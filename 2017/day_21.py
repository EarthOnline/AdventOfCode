from typing import Dict

INPUT = open("./input_files/input_21", "r").read().strip("\n")


def rotate(input: str) -> str:
    if len(input) == 5:
        return input[3] + input[0] + input[2] + input[4] + input[1]
    if len(input) == 11:
        return input[8] + input[4] + input[0] + input[3] + input[9] + input[5] + input[1] + input[7] + input[10] + input[6] + input[2]
    return ''


def flip(input: str) -> str:
    return "/".join(input.split("/")[::-1])


def build_instructions(instruct_input: str) -> Dict[str, str]:
    instructions = dict()
    for _i, instruction in enumerate(instruct_input.split("\n")):
        input, _x, output = instruction.split(" ")

        for x in range(4):
            input = rotate(input)
            instructions[input] = output
            instructions[flip(input)] = output
    return instructions


def get_burning_pixels(iters):
    instructions = build_instructions(INPUT)
    pattern = ".#./..#/###"

    for x in range(iters):
        width = pattern.index("/")
        size = 2 if width % 2 == 0 else 3
        factor = width // size

        patterns = list()

        p = pattern.split('/')
        for r in range(factor):
            for c in range(factor):
                pat = list()
                pat.append(p[r * size][c * size:(c + 1) * size])
                pat.append(p[r * size + 1][c * size:(c + 1) * size])
                if size == 3:
                    pat.append(p[r * size + 2][c * size:(c + 1) * size])
                patterns.append("/".join(pat))

        new_patterns = [instructions[p] for p in patterns]
        new_size = size + 1

        new_pattern = ["" for r in range(new_size * factor)]

        for index, np in enumerate(new_patterns):
            row = (index // factor) * new_size
            for rindex, r in enumerate(np.split("/")):
                new_pattern[row + rindex] += r

        pattern = "/".join(new_pattern)
    return len([x for x in pattern if x == '#'])


def run_1():
    return get_burning_pixels(5)


def run_2():
    return get_burning_pixels(18)


print(run_1())
print(run_2())
