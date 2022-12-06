import string

INPUT = open("./input_files/input_25", "r").read().strip("\n")

POSITION = [int(x[:-1]) for x in INPUT.split(' ') if len(x) > 0 and x[0] in string.digits]


def line_one(column):
    return sum(range(column + 1))


def line_n(row, column):
    start = line_one(column)
    return start + sum(range(column, row + column - 1))


def run_1():
    number = line_n(*POSITION)
    data = 20151125
    while number > 1:
        number -= 1
        data = data * 252533 % 33554393
    return data


def run_2():
    return


print(run_1())
print(run_2())
