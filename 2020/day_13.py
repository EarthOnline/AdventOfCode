from functools import reduce

INPUT = open("./input_files/input_13", "r").read().strip("\n")

START = int(INPUT.split('\n')[0])
BUSSES = [int(x) for x in INPUT.split('\n')[1].replace('x,', '').split(',')]
TIMES = [int(x) if x.isnumeric() else x for x in INPUT.split('\n')[1].split(',')]


def run_1():
    time_to_leave = {k: v for k, v in map(lambda b: (b, b - START % b), BUSSES)}
    return [k * v for k, v in time_to_leave.items() if v == min(time_to_leave.values())][0]


def run_2():
    schedule = {b: i for i, b in enumerate(TIMES) if b != 'x'}
    step_size = 1
    time = 0
    matches = 0
    while True:
        time += step_size

        busses = [bus for bus, offset in schedule.items() if (time + offset) % bus == 0]
        meets = len(busses)

        if meets == len(schedule):
            break

        if meets > matches:
            matches = meets
            step_size = reduce(lambda x, y: x * y, busses)

    return time


print(run_1())
print(run_2())
