from collections import defaultdict

INPUT = open("./input_files/input_11", "r").read().strip("\n")


def run_1():
    steps = INPUT.split(",")
    grouped = defaultdict(int)

    for step in steps:
        grouped[step] += 1

    equalizers = [('s', 'n'), ('se', 'nw'), ('sw', 'ne')]

    for equalizer in equalizers:
        if grouped[equalizer[0]] > grouped[equalizer[1]]:
            grouped[equalizer[0]] -= grouped[equalizer[1]]
            grouped[equalizer[1]] = 0
        else:
            grouped[equalizer[1]] -= grouped[equalizer[0]]
            grouped[equalizer[0]] = 0

    equalizers = [('se', 'n', 'ne'), ('sw', 'n', 'nw'), ('ne', 's', 'se'), ('nw', 's', 'sw')]

    for equalizer in equalizers:
        if grouped[equalizer[1]] == 0:
            continue
        equalize = min(grouped[equalizer[0]], grouped[equalizer[1]])
        grouped[equalizer[0]] -= equalize
        grouped[equalizer[1]] -= equalize
        grouped[equalizer[2]] += equalize

    return sum(grouped.values())


def run_2():
    steps = INPUT.split(",")
    grouped = defaultdict(int)
    value_per_step = list()

    for step in steps:
        grouped[step] += 1

        equalizers = [('se', 'n', 'ne'), ('sw', 'n', 'nw'), ('ne', 's', 'se'), ('nw', 's', 'sw')]

        for equalizer in equalizers:
            if grouped[equalizer[1]] == 0:
                continue
            equalize = min(grouped[equalizer[0]], grouped[equalizer[1]])
            grouped[equalizer[0]] -= equalize
            grouped[equalizer[1]] -= equalize
            grouped[equalizer[2]] += equalize

        equalizers = [('s', 'n'), ('se', 'nw'), ('sw', 'ne')]

        for equalizer in equalizers:
            if grouped[equalizer[0]] > grouped[equalizer[1]]:
                grouped[equalizer[0]] -= grouped[equalizer[1]]
                grouped[equalizer[1]] = 0
            else:
                grouped[equalizer[1]] -= grouped[equalizer[0]]
                grouped[equalizer[0]] = 0

        equalizers = [('se', 'sw', 's'), ('ne', 'nw', 'n')]

        for equalizer in equalizers:
            equalize = min(grouped[equalizer[0]], grouped[equalizer[0]])
            grouped[equalizer[0]] -= equalize
            grouped[equalizer[1]] -= equalize
            grouped[equalizer[2]] += equalize

        value_per_step.append(sum(grouped.values()))

    return max(value_per_step)


print(run_1())
print(run_2())
