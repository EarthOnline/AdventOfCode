INPUT = open("./input_files/input_09", "r").read().strip("\n")


XMAS = [int(x) for x in INPUT.split('\n')]


def check_for_sum(value, check_set):
    return len(
        [c for idx, c in enumerate(check_set) if value - c in [x for i, x in enumerate(check_set) if i != idx]]
    ) > 1


def run_1():
    for i, x in enumerate(XMAS[25:]):
        check_set = XMAS[i:i + 25]
        if not check_for_sum(x, check_set):
            break
    return x


def run_2():
    invalid_number = run_1()

    for i in range(len(XMAS)):
        slice = list()
        size = 0
        while sum(slice) < invalid_number:
            size += 1
            slice = XMAS[i:i + size]
        if sum(slice) == invalid_number:
            break

    return min(slice) + max(slice)


print(run_1())
print(run_2())
