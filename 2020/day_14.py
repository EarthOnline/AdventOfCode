from itertools import combinations

INPUT = open("./input_files/input_14", "r").read().strip("\n")
# INPUT = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1"""


def run_1():
    memory = dict()
    mask = None

    for line in INPUT.split('\n'):
        instruction, value = line.split(' = ')
        if instruction == 'mask':
            mask = value
            continue

        bin_value = f'{bin(int(value))[2:]:0>36}'
        bin_value = ''.join(map(lambda m, v: v if m == 'X' else m, mask, bin_value))
        memory[instruction[4:-1]] = int(bin_value, 2)

    return sum(memory.values())


def run_2():
    memory = dict()
    mask = list()

    for line in INPUT.split('\n'):
        instruction, value = line.split(' = ')
        if instruction == 'mask':
            mask = value
            continue

        bin_value = f'{bin(int(instruction[4:-1]))[2:]:0>36}'
        base_adress = int(''.join(map(lambda m, v: v if m == '0' else '0' if m == 'X' else m, mask, bin_value)), 2)
        to_replace = [2**i for i, x in enumerate(mask[::-1]) if x == 'X']
        combos = [0]
        for r in range(len(to_replace)):
            combos.extend(sum(x) for x in combinations(to_replace, r + 1))

        for combo in combos:
            adress = base_adress + combo
            memory[adress] = int(value)

    return sum(memory.values())


print(run_1())
print(run_2())
