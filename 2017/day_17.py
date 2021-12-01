INPUT = 370


def run_1():
    buffer = [0]
    pointer = 0

    for x in range(2017):
        pointer = (pointer + INPUT) % len(buffer)
        buffer.insert(pointer + 1, x + 1)
        pointer += 1
    return buffer[buffer.index(2017) + 1]


def run_2():
    pointer = 0
    next_value = None

    for x in range(1, 50000000 + 1):
        pointer = (pointer + INPUT) % x + 1
        if pointer == 1:
            next_value = x
    return next_value


print(run_1())
print(run_2())
