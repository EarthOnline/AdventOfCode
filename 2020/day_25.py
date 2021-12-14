INPUT = open("./input_files/input_25", "r").read().strip("\n")
# INPUT = """5764801
# 17807724"""
CARD_PUB_KEY = int(INPUT.split('\n')[0])
DOOR_PUB_KEY = int(INPUT.split('\n')[1])


def find_loop_size(subject_number, pub_key):
    value = 1
    loop_size = 0
    while value != pub_key:
        loop_size += 1
        value *= subject_number
        value = value % 20201227
    return loop_size


def run_1():
    subject_number = 7
    card_loop = find_loop_size(subject_number, CARD_PUB_KEY)
    door_loop = find_loop_size(subject_number, DOOR_PUB_KEY)

    value = 1
    for _ in range(door_loop):
        value *= CARD_PUB_KEY
        value = value % 20201227
    return value


def run_2():
    return


print(run_1())
print(run_2())
