INPUT = open("./input_files/input_01", "r").read().strip("\n")

MASS_LIST = [int(x) for x in INPUT.split("\n")]


def fuel_req(mass: int) -> int:
    return mass//3-2


def total_fuel_req(mass: int) -> int:
    total_fuel = fuel_req(mass)
    added_fuel = total_fuel
    while added_fuel > 0:
        fuel_mass = max(0, fuel_req(added_fuel))
        total_fuel += fuel_mass
        added_fuel = fuel_mass
    return total_fuel


def run_1():
    return sum([fuel_req(mass) for mass in MASS_LIST])


def run_2():
    return sum([total_fuel_req(mass) for mass in MASS_LIST])


print(run_1())
print(run_2())
