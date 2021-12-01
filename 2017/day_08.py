from collections import defaultdict


INPUT = open("./input_files/input_08", "r").read().strip("\n")


def check_condition(register, address, opperator, amount):
    if opperator == "==":
        return register[address] == amount
    if opperator == "<=":
        return register[address] <= amount
    if opperator == "!=":
        return register[address] != amount
    if opperator == ">=":
        return register[address] >= amount
    if opperator == "<":
        return register[address] < amount
    if opperator == ">":
        return register[address] > amount
    raise NotImplementedError(opperator)


def run_1():
    register = defaultdict(int)

    for instruction in INPUT.split("\n"):
        address, opperation, amount, _if, condition_address, contition_opperator, condition_amount = \
            instruction.split(" ")
        if check_condition(register, condition_address, contition_opperator, int(condition_amount)):
            if opperation == 'inc':
                register[address] += int(amount)
            if opperation == 'dec':
                register[address] -= int(amount)

    return max(register.values())


def run_2():
    register = defaultdict(int)
    max_per_instruction = list()

    for instruction in INPUT.split("\n"):
        address, opperation, amount, _if, condition_address, contition_opperator, condition_amount = \
            instruction.split(" ")
        if check_condition(register, condition_address, contition_opperator, int(condition_amount)):
            if opperation == 'inc':
                register[address] += int(amount)
            if opperation == 'dec':
                register[address] -= int(amount)
        max_per_instruction.append(max(register.values()))
    return max(max_per_instruction)


print(run_1())
print(run_2())
