INPUT = open("./input_files/input_04", "r").read().strip("\n")


def run_1():
    result = 0
    passphrases = INPUT.split("\n")
    for passphrase in passphrases:
        items = passphrase.split(" ")
        words = set(items)
        result += 1 if len(words) == len(items) else 0
    return result


def run_2():
    result = 0
    passphrases = INPUT.split("\n")
    for passphrase in passphrases:
        items = list()
        for item in passphrase.split(" "):
            broken_item = list(item)
            broken_item.sort()
            items.append(''.join(broken_item))
        words = set(items)
        result += 1 if len(words) == len(items) else 0
    return result


print(run_1())
print(run_2())
