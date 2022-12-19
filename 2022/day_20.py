from time import time

start = time()
INPUT = open("./input_files/input_20", "r").read().strip("\n")


def run_1():
    return INPUT


def run_2():
    return


print(run_1())
print('==> ', (time() - start) * 1000)
print(run_2())
print('==> ', (time() - start) * 1000)
