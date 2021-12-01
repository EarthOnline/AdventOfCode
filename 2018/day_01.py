INPUT = open("./input_files/input_01", "r").read().strip("\n")


CHANGE_LIST = [int(x) for x in INPUT.split("\n")]


def run_1():
    return sum(CHANGE_LIST)


def run_2():
    current_frequency = 0
    past_frequencies = set()

    index = 0

    while current_frequency not in past_frequencies:
        past_frequencies.add(current_frequency)
        current_frequency += CHANGE_LIST[index % len(CHANGE_LIST)]
        index += 1
    return current_frequency


print(run_1())
print(run_2())
