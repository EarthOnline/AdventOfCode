from typing import List

INPUT = open("./input_files/input_03", "r").read().strip("\n")
# INPUT = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
DIAGNOSTICS = INPUT.split('\n')


def run_1():
    positions = [[d[x] for d in DIAGNOSTICS] for x in range(len(DIAGNOSTICS[0]))]
    gamma = int(''.join(map(lambda x: max(set(x), key=x.count), positions)), 2)
    epsylon = int(''.join(map(lambda x: min(set(x), key=x.count), positions)), 2)

    return gamma * epsylon


def count_bias(options: List[str], option: str, bias: str):
    counted = options.count(option)
    return counted + .1 if option == bias else counted


def run_2():
    ogr = DIAGNOSTICS
    csr = DIAGNOSTICS

    position = 0
    while len(ogr) > 1:
        options = [d[position] for d in ogr]
        max_bit = max(set(options), key=lambda x: count_bias(options, x, '1'))
        ogr = [d for d in ogr if d[position] == max_bit]
        position += 1

    position = 0
    while len(csr) > 1:
        options = [d[position] for d in csr]
        # min_bit = min(options, key=options.count)
        # min_bit = '0' if len(options) % 2 == 0 and options.count(min_bit) == len(options) // 2 else min_bit
        min_bit = min(set(options), key=lambda x: count_bias(options, x, '1'))
        csr = [d for d in csr if d[position] == min_bit]
        position += 1

    return int(''.join(ogr), 2) * int(''.join(csr), 2)


print(run_1())
print(run_2())
