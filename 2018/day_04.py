from collections import defaultdict
from typing import Dict, List, Tuple

INPUT = open("./input_files/input_04", "r").read().strip("\n")


ORDERED_NOTES = sorted(INPUT.split("\n"))


def get_sleep_patterns() -> Dict[str, List[Tuple[int, int]]]:
    sleep_patterns = defaultdict(list)
    selected_guard = None
    start_sleep = None
    for note in ORDERED_NOTES:
        if 'begins shift' in note:
            selected_guard = note.split(" ")[3]
        elif 'falls asleep' in note:
            start_sleep = int(note[15:17])
        elif 'wakes up' in note:
            end_sleep = int(note[15:17])
            sleep_patterns[selected_guard].append((start_sleep, end_sleep))
    return sleep_patterns


def get_sleepiest_minute(sleep_pattern: List[Tuple[int, int]]) -> Tuple[int, int]:
    night = defaultdict(int)
    for sleep in sleep_pattern:
        for minute in range(sleep[0], sleep[1]):
            night[minute] += 1

    most_asleep = max(night.values())
    return [(k, most_asleep) for k, v in night.items() if v == most_asleep][0]


def run_1():
    sleep_patterns = get_sleep_patterns()
    minutes_of_sleep = {sum([s[1] - s[0] for s in v]): k for k, v in sleep_patterns.items()}

    longest_sleep = max(minutes_of_sleep.keys())
    sleepiest_guard = minutes_of_sleep[longest_sleep]

    sleepiest_minute = get_sleepiest_minute(sleep_patterns[sleepiest_guard])[0]
    return int(sleepiest_guard[1:]) * sleepiest_minute


def run_2():
    sleep_patterns = get_sleep_patterns()

    max_count = 0
    selected_guard = None
    selected_minute = None

    for guard, sleep_pattern in sleep_patterns.items():
        minute, count = get_sleepiest_minute(sleep_pattern)
        if count > max_count:
            max_count = count
            selected_guard = guard
            selected_minute = minute

    return int(selected_guard[1:]) * selected_minute


print(run_1())
print(run_2())
