INPUT = open("./input_files/input_14", "r").read().strip("\n")
# INPUT = """NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""
TEMPLATE = INPUT.split('\n\n')[0]
RULES = {k: v for k, v in [x.split(' -> ') for x in INPUT.split('\n\n')[1].split('\n')]}


def step(template):
    pairs = [template[x:x+2] for x in range(len(template) - 1)]

    new_template = template[0]
    for i, m in enumerate([RULES[x] for x in pairs], 1):
        new_template += m + template[i]
    return new_template


def run_1():
    template = TEMPLATE
    for _ in range(10):
        template = step(template)

    elements = [template.count(e) for e in set(template)]
    return max(elements) - min(elements)


def split_pair(pair):
    found = RULES[pair]
    return pair[0]+found, found+pair[1]


def run_2():
    pairs = [TEMPLATE[x:x + 2] for x in range(len(TEMPLATE) - 1)]
    pair_count = {x: pairs.count(x) for x in RULES.keys()}

    for _ in range(40):
        new_pairs = {x: 0 for x in RULES.keys()}
        for pair, count in pair_count.items():
            p1, p2 = split_pair(pair)
            new_pairs[p1] += count
            new_pairs[p2] += count

        pair_count = new_pairs
    element_count = {x: 0 for x in set(RULES.values())}
    for k, v in pair_count.items():
        element_count[k[0]] += v
        element_count[k[1]] += v

    element_count[TEMPLATE[0]] += 1
    element_count[TEMPLATE[-1]] += 1
    element_count = {k: v // 2 for k, v in element_count.items()}
    return max(element_count.values()) - min(element_count.values())


print(run_1())
print(run_2())
