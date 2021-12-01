import itertools
import math
from collections import defaultdict
from copy import deepcopy, copy
from functools import reduce

INPUT = open("./input_files/input_20", "r").read().strip("\n")


def get_label(x, y):
    x += 2
    y += 2
    lines = INPUT.split('\n')

    tries = [(x - 1, y, f'{lines[y][x - 2]}{lines[y][x - 1]}'),
             (x + 1, y, f'{lines[y][x + 1]}{lines[y][x + 2]}'),
             (x, y - 1, f'{lines[y - 2][x]}{lines[y - 1][x]}'),
             (x, y + 1, f'{lines[y + 1][x]}{lines[y + 2][x]}')]

    for x, y, label in tries:
        if lines[y][x] not in [' ', '.', '#']:
            return label
    return None


def get_maze():
    maze = dict()
    portals = dict()
    lines = INPUT.split('\n')
    for y, line in enumerate(lines[2:-2]):
        for x, value in enumerate(line[2:-2]):
            if value == '.':
                label = get_label(x, y)
                if label is not None:
                    portals[(x, y)] = label

            if value in ['#', '.']:
                maze[(x, y)] = value
    return maze, portals


MAZE, PORTALS = get_maze()


def can_step(maze, x, y):
    current_value = maze[(x, y)]
    if current_value != '.':
        return False

    location = (x, y)
    if location in PORTALS.keys():
        portal = PORTALS[(x, y)]
        if portal not in ['AA', 'ZZ']:
            other_portal = [l for l, v in PORTALS.items() if v == portal and l != location][0]
            if maze[other_portal] == 'X':
                return True

    return any([maze.get((x, y - 1), ' ') == 'X',
                maze.get((x, y + 1), ' ') == 'X',
                maze.get((x - 1, y), ' ') == 'X',
                maze.get((x + 1, y), ' ') == 'X'])


def print_maze(maze):
    print('-----')
    xs = [x for x, y in maze.keys()]
    ys = [y for x, y in maze.keys()]

    for y in range(min(ys), max(ys) + 1):
        print(' '.join([maze.get((x, y), ' ') for x in range(min(xs), max(xs) + 1)]))
    print('-----')


def run_1():
    steps = 0
    maze = copy(MAZE)
    start = [l for l, v in PORTALS.items() if v == 'AA'][0]
    maze[start] = 'X'

    end = [l for l, v in PORTALS.items() if v == 'ZZ'][0]

    while maze[end] != 'X':
        new_maze = {l: v for l, v in maze.items() if v in ['#', 'X']}
        for location, value in {l: v for l, v in maze.items() if v not in ['#', 'X']}.items():
            if can_step(maze, location[0], location[1]):
                new_maze[location] = 'X'
                continue
            new_maze[location] = value
        maze = new_maze
        # print_maze(maze)
        steps += 1
    return steps


def run_2():
    return None


print(run_1())
print(run_2())
