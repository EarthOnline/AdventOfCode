INPUT = open("./input_files/input_06", "r").read().strip("\n")


def unique_detector(stream, length):
    for index in range(len(stream)):
        subset = stream[index: index + length]
        if len(set(subset)) == length:
            return index + length
    return None


def run_1():
    return unique_detector(INPUT, 4)


def run_2():
    return unique_detector(INPUT, 14)


print(run_1())
print(run_2())
