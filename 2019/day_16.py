import itertools
import math
from collections import defaultdict
from copy import deepcopy
from functools import reduce

INPUT = open("./input_files/input_16", "r").read().strip("\n")
# INPUT = '80871224585914546619083218645595'

SIGNAL = [int(x) for x in INPUT]


def fft_run(input):
    for _ in range(100):
        output = list()
        i = 0
        while i < len(input):
            i += 1
            pattern_length = i * 4

            def positive(x):
                return i - 1 <= x % pattern_length < i + i - 1

            def negative(x):
                return i * 3 - 1 <= x % pattern_length < i * 4 - 1

            result = sum(c for p, c in enumerate(input) if positive(p)) \
                - sum(c for p, c in enumerate(input) if negative(p))
            output.append(abs(result) % 10)
        input = output

    return input


def run_1():
    input = fft_run(SIGNAL)

    return ''.join([str(x) for x in input[:8]])


def run_2():
    input = list()
    for _ in range(10000):
        input.extend(SIGNAL)
    position = ''.join([str(x) for x in input[:7]])

    input = fft_run(input)

    return ''.join([str(x) for x in input[position:position + 8]])


print(run_1())
print(run_2())
