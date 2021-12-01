INPUT = open("./input_files/input_01", "r").read().strip("\n")


def run_1():
    result = 0
    pref_number = int(INPUT[-1:])
    for _number in INPUT:
        number = int(_number)
        if pref_number == number:
            result += number
        pref_number = number
    return result


def run_2():
    result = 0
    offset = int(len(INPUT) / 2)
    for _index, _number in enumerate(INPUT):
        number = int(_number)
        compare_to = int(INPUT[(_index - offset):None if (_index - offset) == -1 else (_index - offset + 1)])
        if number == compare_to:
            result += number
    return result


print(run_1())
print(run_2())
