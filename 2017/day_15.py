from typing import List, Callable

INPUT = open("./input_files/input_15", "r").read().strip("\n")


def generate(value: int, factor: int) -> int:
    return value * factor % 2147483647


def judge(list_a: List[int], list_b: List[int]) -> List[bool]:
    return list(map(lambda x, y: x == y, list_a, list_b))


def run_1():
    generator_values = [int(x.split(" ")[-1]) for x in INPUT.split("\n")]
    current_value_a = generator_values[0]  # 65
    current_value_b = generator_values[1]  # 8921

    factor_a = 16807
    factor_b = 48271

    size = 40000000
    roof = 2 ** 16

    count = 0

    for x in range(size):
        current_value_a = generate(current_value_a, factor_a)
        current_value_b = generate(current_value_b, factor_b)
        count += 1 if current_value_a % roof == current_value_b % roof else 0

    return count


def generate_list(start_value: int, factor: int, size: int, condition: Callable[[int], bool]) -> List[int]:
    roof = 2 ** 16

    generated_list = list()
    current_value = start_value

    while len(generated_list) < size:
        current_value = generate(current_value, factor)
        if condition(current_value):
            generated_list.append(current_value % roof)

    return generated_list


def run_2():
    generator_values = [int(x.split(" ")[-1]) for x in INPUT.split("\n")]
    start_value_a = generator_values[0]  # 65
    start_value_b = generator_values[1]  # 8921

    factor_a = 16807
    factor_b = 48271

    size = 5000000

    values_a = generate_list(start_value_a, factor_a, size, lambda x: x % 4 == 0)
    values_b = generate_list(start_value_b, factor_b, size, lambda x: x % 8 == 0)

    return len([x for x in judge(values_a, values_b) if x])


print(run_1())
print(run_2())
