INPUT = open("./input_files/input_06", "r").read()


def get_memory_key(memorybank):
    return ":".join([str(x) for x in memorybank])


def clean_memory(memorybank):
    steps = max(memorybank)
    index = memorybank.index(steps)
    memorybank[index] = 0

    while steps:
        index = (index + 1) % len(memorybank)
        memorybank[index] += 1
        steps -= 1


def run_1():
    memorybank = [int(x) for x in INPUT.split("\t")]
    memorylog = list()

    while True:
        memorykey = get_memory_key(memorybank)
        if memorykey in memorylog:
            break
        memorylog.append(memorykey)
        clean_memory(memorybank)
    return len(memorylog)


def run_2():
    memorybank = [int(x) for x in INPUT.split("\t")]
    memorylog = list()

    while True:
        memorykey = get_memory_key(memorybank)
        if memorykey in memorylog:
            break
        memorylog.append(memorykey)
        clean_memory(memorybank)
    return len(memorylog) - memorylog.index(get_memory_key(memorybank))


print(run_1())
print(run_2())
