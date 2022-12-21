from time import time

start = time()
INPUT = open("./input_files/input_22", "r").read().strip("\n")


def run_1():
    return INPUT


def run_2():
    return


print('\n', 'Part 1 ==> ', run_1())
print(f'in {int((time() - start) * 1000)} ms')
print('\n', 'Part 2 ==> ', run_2())
print(f'in {int((time() - start) * 1000)} ms')
