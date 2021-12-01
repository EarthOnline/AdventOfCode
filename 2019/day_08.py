from copy import copy

INPUT = open("./input_files/input_08", "r").read().strip("\n")

N = 25
R = 6
L = N * R

LAYERS = [[s[i: i + N] for i in range(0, len(s), N)] for s in [INPUT[i: i + L] for i in range(0, len(INPUT), L)]]


def run_1():
    zero_count = [sum([r.count('0') for r in l]) for l in LAYERS]
    min_count = min(zero_count)
    min_layer = LAYERS[zero_count.index(min_count)]
    one_count = sum([r.count('1') for r in min_layer])
    two_count = sum([r.count('2') for r in min_layer])
    return one_count * two_count


def print_image(image):
    image = copy(image)
    print('-------------------------')
    for r in image:
        row = ''.join(r)
        row = row.replace('.', ' ')
        print(row)
    print('-------------------------')


def run_2():
    layers = LAYERS[::-1]
    image = [[' ' for n in range(N)] for r in range(R)]

    for l, layer in enumerate(layers):
        for r, row in enumerate(layer):
            for p, pixel in enumerate(row):
                if pixel == '2':
                    continue

                image[r][p] = '.' if pixel == '0' else 'X'
    print_image(image)
    return


print(run_1())
print(run_2())
