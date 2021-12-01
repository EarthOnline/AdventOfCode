INPUT = open("./input_files/input_09", "r").read()


def run_1():
    result = 0

    ignore = False
    garbage = False
    level = 0
    for char in INPUT:
        if ignore:
            ignore = False
            continue
        if char == "!":
            ignore = True
            continue
        if not garbage and char == "{":
            level += 1
            continue
        if not garbage and char == "}":
            result += level
            level -= 1
            continue
        if char == "<":
            garbage = True
            continue
        if char == ">":
            garbage = False
            continue
    return result


def run_2():
    result = 0

    ignore = False
    garbage = False
    level = 0
    for char in INPUT:
        if ignore:
            ignore = False
            continue
        if char == "!":
            ignore = True
            continue
        if not garbage and char == "<":
            garbage = True
            continue
        if char == ">":
            garbage = False
            continue
        if garbage:
            result += 1
    return result


print(run_1())
print(run_2())
