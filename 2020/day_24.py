from itertools import chain

INPUT = open("./input_files/input_24", "r").read().strip("\n")
# INPUT = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew"""


def simple_path(directions):
    path = {
        'ne': directions.count('ne'),
        'se': directions.count('se'),
        'e': directions.count('e') - directions.count('ne') - directions.count('se'),
        'nw': directions.count('nw'),
        'sw': directions.count('sw'),
        'w': directions.count('w') - directions.count('nw') - directions.count('sw'),
    }

    nesw = min(path['ne'], path['sw'])
    path['ne'] -= nesw
    path['sw'] -= nesw

    nwse = min(path['nw'], path['se'])
    path['nw'] -= nwse
    path['se'] -= nwse

    nese = min(path['ne'], path['se'])
    path['ne'] -= nese
    path['se'] -= nese
    path['e'] += nese

    nwsw = min(path['nw'], path['sw'])
    path['nw'] -= nwsw
    path['sw'] -= nwsw
    path['w'] += nwsw

    ew = min(path['e'], path['w'])
    path['e'] -= ew
    path['w'] -= ew

    new = min(path['ne'], path['w'])
    path['ne'] -= new
    path['w'] -= new
    path['nw'] += new

    nwe = min(path['nw'], path['e'])
    path['nw'] -= nwe
    path['e'] -= nwe
    path['ne'] += nwe

    sew = min(path['se'], path['w'])
    path['se'] -= sew
    path['w'] -= sew
    path['sw'] += sew

    swe = min(path['sw'], path['e'])
    path['sw'] -= swe
    path['e'] -= swe
    path['se'] += swe

    directions = ''
    for key in sorted(path.keys()):
        for _ in range(path[key]):
            directions += key
    return directions


PATHS = [simple_path(x) for x in INPUT.split('\n')]


def run_1():
    return sum(PATHS.count(p) % 2 == 1 for p in set(PATHS))


def adjecent_tiles(path):
    return [simple_path(path + x) for x in ['ne', 'nw', 'e', 'se', 'sw', 'w']]


def run_2():
    black_tiles = [p for p in set(PATHS) if PATHS.count(p) % 2 == 1]

    for _ in range(100):
        adjecents = {b: adjecent_tiles(b) for b in black_tiles}
        flip_to_white = [b for b, a in adjecents.items() if sum(t in black_tiles for t in a) not in [1, 2]]
        all_adjecents = list(chain.from_iterable(adjecents.values()))
        flip_to_black = [t for t in set(all_adjecents) if all_adjecents.count(t) == 2]
        black_tiles = set([b for b in black_tiles if b not in flip_to_white] + flip_to_black)

    return len(black_tiles)


print(run_1())
print(run_2())
