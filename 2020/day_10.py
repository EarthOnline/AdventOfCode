INPUT = open("./input_files/input_10", "r").read().strip("\n")


ADAPTERS = [int(a) for a in INPUT.split('\n')]


def run_1():
    chain = sorted(ADAPTERS + [0, max(ADAPTERS) + 3])
    return len([c for c in chain if c - 1 in chain]) * \
        len([c for c in chain if c > 2 and c - 1 not in chain and c - 2 not in chain])


def run_2():
    chain = sorted(ADAPTERS)
    chain.append(chain[-1] + 3)
    steps = dict()
    steps[0] = 1
    for adapter in chain:
        steps[adapter] = sum(steps[x] for x in [adapter - 1, adapter - 2, adapter - 3] if x in steps)
    return steps[max(steps.keys())]


print(run_1())
print(run_2())
