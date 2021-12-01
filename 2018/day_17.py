from collections import defaultdict
from typing import Dict, Tuple

INPUT = open("./input_files/input_17", "r").read().strip("\n")
# INPUT = """x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=2..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504"""


SPRING = (500, 0)

CLAY = "#"
WET = "~"
DRIP = '|'
SAND = "."


def get_scan() -> Dict[Tuple[int, int], str]:
    scan = dict()
    for line in INPUT.splitlines():
        clay_point, clay_range = line.split(", ")
        horizontal = clay_point[:1] == 'x'
        cpoint = int(clay_point[2:])
        cstart, cend = [int(x) for x in clay_range[2:].split("..")]
        crange = range(cstart, cend + 1)
        for r in crange:
            location = (cpoint, r) if horizontal else (r, cpoint)
            scan[location] = CLAY
    return scan


SCAN = get_scan()


def activate_source(area, min_x, max_x, min_y, max_y):
    source = SPRING

    falling_water = defaultdict(set)
    falling_water[min_y].add(source[0])
    y = min_y

    while y <= max_y:
        # print(max_y - y)
        # for _y in range(y - 5, y + 5):
        #     print(''.join([area.get((x, _y), SAND) for x in range(min_x - 1, max_x + 2)]))
        # print('---')
        for x in falling_water[y]:
            material = area.get((x, y), SAND)
            if material in [SAND, DRIP]:
                area[(x, y)] = DRIP
                falling_water[y + 1].add(x)
            else:
                left_up = False
                right_up = False
                for lx in range(1000):
                    lmaterial = area.get((x - lx, y), SAND)
                    lmaterial_up = area.get((x - lx, y - 1), SAND)
                    if lmaterial in [WET, CLAY] and lmaterial_up in [SAND, DRIP]:
                        area[x - lx, y-1] = DRIP
                        continue
                    if lmaterial in [SAND, DRIP]:
                        area[x - lx, y - 1] = DRIP
                        area[x - lx, y] = DRIP
                        falling_water[y + 1].add(x - lx)
                        break
                    if lmaterial_up == CLAY:
                        left_up = x - lx + 1
                        break
                for rx in range(1, 1000):
                    rmaterial = area.get((x + rx, y), SAND)
                    rmaterial_up = area.get((x + rx, y - 1), SAND)
                    if rmaterial in [WET, CLAY] and rmaterial_up in [SAND, DRIP]:
                        area[x + rx, y-1] = DRIP
                        continue
                    if rmaterial in [SAND, DRIP]:
                        area[x + rx, y - 1] = DRIP
                        area[x + rx, y] = DRIP
                        falling_water[y + 1].add(x + rx)
                        break
                    if rmaterial_up == CLAY:
                        right_up = x + rx - 1
                        break
                if left_up and right_up:
                    for nx in range(left_up, right_up + 1):
                        if nx in falling_water[y]:
                            falling_water[y].remove(nx)
                        area[nx, y - 1] = WET
                    y -= 2
                    break
        y += 1
    return area


def run_1():
    min_x = min([x for x, y in SCAN.keys()])
    min_y = min([y for x, y in SCAN.keys()])
    max_x = max([x for x, y in SCAN.keys()])
    max_y = max([y for x, y in SCAN.keys()])

    area = SCAN

    wet_area = activate_source(area, min_x, max_x, min_y, max_y)

    for y in range(min_y, max_y + 1):
        print(''.join([wet_area.get((x, y), SAND) for x in range(min_x - 1, max_x + 2)]))

    return sum([1 for (x, y), v in wet_area.items() if v in [WET, DRIP]]), \
        sum([1 for (x, y), v in wet_area.items() if v in [WET]])


print(run_1())
