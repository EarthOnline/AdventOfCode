from copy import copy
from string import ascii_lowercase, ascii_uppercase

INPUT = open("./input_files/input_18", "r").read().strip("\n")
# INPUT_2 = open("input_files/input_15_2", "r").read().strip("\n")
INPUT = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""


def print_map(grid_map):
    print('---')
    for line in grid_map:
        print(line)
    print('---')


def neighbour_has_step(grid, x, y):
    if grid[y - 1][x] == '@':
        return True
    if grid[y + 1][x] == '@':
        return True
    if grid[y][x - 1] == '@':
        return True
    if grid[y][x + 1] == '@':
        return True
    return False


def get_shortest_path(grid_map, all_keys, keys):
    if keys == all_keys:
        return 0

    old_map = grid_map
    new_map = list()
    moved = False
    for y, line in enumerate(old_map):
        new_line = list()
        for x, location in enumerate(line):
            if location in ['#', '@'] or not neighbour_has_step(old_map, x, y):
                new_line.append(location)
                continue

            if location == '.' or :
                new_line.append('@')
                moved = True
            elif location in ascii_uppercase:
                if location.lower() in keys:
                    new_line.append('@')
                    moved = True
                else:
                    new_line.append(location)
            else:
                print()



def run_1():
    all_keys = set(c for c in INPUT if c in ascii_lowercase)
    grid_map = INPUT.split("\n")
    print_map(grid_map)
    return get_shortest_path(grid_map, all_keys, set())


# def run_2():
#     int_sequence = copy(INT_SEQUENCE)
#     int_sequence[0] = 2
#
#     inst = 'R,10,L,8,R,10,R,4,' \
#            'L,6,L,6,R,10,' \
#            'R,10,L,8,R,10,R,4,' \
#            'L,6,R,12,R,12,R,10,' \
#            'L,6,L,6,R,10,' \
#            'L,6,R,12,R,12,R,10,' \
#            'R,10,L,8,R,10,R,4,' \
#            'L,6,L,6,R,10,' \
#            'R,10,L,8,R,10,R,4,' \
#            'L,6,R,12,R,12,R,10'
#
#     main = 'A,B,A,C,B,C,A,B,A,C\n'
#     func_a = 'R,10,L,8,R,10,R,4\n'
#     func_b = 'L,6,L,6,R,10\n'
#     func_c = 'L,6,R,12,R,12,R,10\n'
#     video = 'n\n'
#
#     input = main + func_a + func_b + func_c + video
#     input = [ord(c) for c in input]
#
#     IOPort.clear_instances()
#     name = f'day_17_2'
#     io = IOPort.get_instance(name)
#     io.inputs = input
#     run_program(name, int_sequence)
#     return io.get_output()


print(run_1())
# print(run_2())
