from json import loads

INPUT = open("./input_files/input_12", "r").read().strip("\n")


def count_values(something) -> int:
    some_type = type(something)
    if some_type == list:
        return sum([count_values(x) for x in something])
    if some_type == str:
        return 0
    if some_type == int:
        return something
    if some_type == dict:
        return sum([count_values(x) for x in something.values()])
    print(some_type)


def count_values_not_red(something) -> int:
    some_type = type(something)
    if some_type == list:
        return sum([count_values_not_red(x) for x in something])
    if some_type == str:
        return 0
    if some_type == int:
        return something
    if some_type == dict:
        if len([x for x in something.values() if x == 'red']):
            return 0
        return sum([count_values_not_red(x) for x in something.values()])
    print(some_type)


def run_1():
    json_object = loads(INPUT)
    return count_values(json_object)


def run_2():
    json_object = loads(INPUT)
    return count_values_not_red(json_object)


print(run_1())
print(run_2())
