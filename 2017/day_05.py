INPUT = open("./input_files/input_05", "r").read().strip("\n")


def run_1():
    memory = [int(x) for x in INPUT.split("\n")]
    pointer = 0
    counter = 0

    while pointer < len(memory):
        old_pointer = pointer
        pointer += memory[pointer]
        memory[old_pointer] += 1
        counter += 1
    return counter


def run_2():
    memory = [int(x) for x in INPUT.split("\n")]
    pointer = 0
    counter = 0

    while pointer < len(memory):
        old_pointer = pointer
        step = memory[pointer]
        pointer += step
        memory[old_pointer] += 1 if step < 3 else -1
        counter += 1
    return counter


print(run_1())
print(run_2())
