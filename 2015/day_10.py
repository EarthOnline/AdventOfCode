from itertools import groupby

INPUT = "3113322113"


def look_and_say(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([f'{len(list(g))}{k}' for k, g in groupby(input_string)])
    return input_string


def run_1():
    return len(look_and_say(INPUT, 40))


def run_2():
    return len(look_and_say(INPUT, 50))


print(run_1())
print(run_2())
