from collections import deque
from time import time

start = time()
INPUT = open("./input_files/input_20", "r").read().strip("\n")


# INPUT = """1
# 2
# -3
# 3
# -2
# 0
# 4"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def set_neighbours(self, _prev, _next):
        self.prev = _prev
        self.next = _next

    def move(self, lenght):
        # Remove from circle
        self.prev.next = self.next
        self.next.prev = self.prev

        # Get place in circle
        self.next = self.next.get_number(self.value % (lenght - 1))
        self.prev = self.next.prev

        # Add self in circle
        self.prev.next = self
        self.next.prev = self

    def get_number(self, steps):
        pointer = self
        while steps > 0:
            pointer = pointer.next
            steps -= 1

        return pointer

    def decode(self):
        return sum(self.get_number(t).value for t in (1000, 2000, 3000))


def run_1():
    numbers = [Node(int(x)) for x in INPUT.split('\n')]
    prev_numbers = deque(numbers)
    prev_numbers.appendleft(prev_numbers.pop())
    next_numbers = deque(numbers)
    next_numbers.append(next_numbers.popleft())
    for _this, _prev, _next in zip(numbers, prev_numbers, next_numbers):
        _this.set_neighbours(_prev, _next)

    lenght = len(numbers)
    zero = [n for n in numbers if n.value == 0][0]
    for node in numbers:
        node.move(lenght)

    return zero.decode()


def run_2():
    numbers = [Node(int(x)) for x in INPUT.split('\n')]
    prev_numbers = deque(numbers)
    prev_numbers.appendleft(prev_numbers.pop())
    next_numbers = deque(numbers)
    next_numbers.append(next_numbers.popleft())
    for _this, _prev, _next in zip(numbers, prev_numbers, next_numbers):
        _this.set_neighbours(_prev, _next)

    zero = [n for n in numbers if n.value == 0][0]
    for node in numbers:
        node.value *= 811589153

    lenght = len(numbers)
    for _ in range(10):
        for node in numbers:
            node.move(lenght)

    return zero.decode()


print(run_1())
print('==> ', (time() - start) * 1000)
print(run_2())
print('==> ', (time() - start) * 1000)
