from itertools import chain

INPUT = open("./input_files/input_21", "r").read().strip("\n")
# INPUT = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)"""


def read_label(text: str):
    part_1, part_2 = text.split(' (contains ')
    return {
        'ingredients': part_1.split(' '),
        'allergens': part_2[:-1].split(', ')
    }


PRODUCTS = [read_label(x) for x in INPUT.split('\n')]


def find_match(allergens, solved):
    for allergen in allergens:
        products = [x['ingredients'] for x in PRODUCTS if allergen in x['allergens']]
        ingredients = list(chain.from_iterable(products))
        possible = [x for x in set(ingredients) if x not in solved.values() and ingredients.count(x) == len(products)]
        if len(possible) == 1:
            return allergen, possible[0]


def get_dangerous_ingredients():
    solved = {}

    allergens = set(chain.from_iterable(x['allergens'] for x in PRODUCTS))
    while len(allergens) > 0:
        allergen, ingredient = find_match(allergens, solved)
        solved[allergen] = ingredient
        allergens.remove(allergen)

    return solved


def run_1():
    solved = get_dangerous_ingredients()
    return len(list(chain.from_iterable([i for i in x['ingredients'] if i not in solved.values()] for x in PRODUCTS)))


def run_2():
    return ','.join(y for x, y in sorted(get_dangerous_ingredients().items(), key=lambda x: x[0]))


print(run_1())
print(run_2())
