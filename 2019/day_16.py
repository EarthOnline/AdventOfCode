import math
from typing import List

INPUT = open("./input_files/input_16", "r").read().strip("\n")
# INPUT = '80871224585914546619083218645595'

SIGNAL = [int(x) for x in INPUT]


def fft_pattern(signal: List[int], position: int) -> List[int]:
    pattern_length = position * 4
    for p, c in enumerate(signal, 1):
        mask = p % pattern_length // position
        if mask == 1:
            yield c
        if mask == 3:
            yield 0 - c


def fft_phase(signal: List[int]):
    for i in range(1, len(signal) + 1):
        yield abs(sum(fft_pattern(signal, i))) % 10


def fft_run(signal: List[int]) -> List[int]:
    for _ in range(100):
        signal = list(fft_phase(signal))
    return signal


def run_1():
    return ''.join([str(x) for x in fft_run(SIGNAL)[:8]])


def run_2():
    signal = SIGNAL * 10000
    position = int(''.join([str(x) for x in signal[:7]]))

    signal = fft_run(signal)

    return ''.join([str(x) for x in signal[position:position + 8]])


print(run_1())
print(run_2())
