INPUT = open("./input_files/input_07", "r").read().strip("\n")


def get_rule(input):
    bag_type, contents = input.split(' bags contain ')
    if contents == 'no other bags.':
        return bag_type, dict()

    contents = contents.replace(' bags', '').replace(' bag', '').replace('.', '').split(', ')
    return bag_type, {' '.join(c[1:]): int(c[0]) for c in [x.split(' ') for x in contents]}


RULES = {k: v for k, v in [get_rule(i) for i in INPUT.split('\n')]}


def can_contain_type(current_bag_type: str, lookup_bag_type: str) -> bool:
    contains = RULES[current_bag_type]
    if lookup_bag_type in contains:
        return True

    return any([can_contain_type(bt, lookup_bag_type) for bt in contains])


def count_contained_bags(current_bag_type: str) -> int:
    contains = RULES[current_bag_type]
    return sum((count_contained_bags(bag) + 1) * ammount for bag, ammount in contains.items())


def run_1():
    return len([bt for bt in RULES.keys() if can_contain_type(bt, 'shiny gold')])


def run_2():
    return count_contained_bags('shiny gold')


print(run_1())
print(run_2())
