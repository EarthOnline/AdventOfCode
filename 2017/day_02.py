INPUT = open("./input_files/input_02", "r").read().strip("\n")


def run_1():
    result = 0
    for row in INPUT.split("\n"):
        cells = [int(c) for c in row.split("\t")]
        result += max(cells) - min(cells)
    return result


def run_2():
    result = 0
    for row in INPUT.split("\n"):
        cells = [int(c) for c in row.split("\t")]
        cells.sort(reverse=True)
        for index, cell in enumerate(cells):
            for devision in cells[index + 1:]:
                if cell % devision == 0:
                    result += cell // devision
    return result


print(run_1())
print(run_2())
